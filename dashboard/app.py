# streamlit run dashboard/app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(
    page_title="MLB Payroll Efficiency Dashboard",
    layout="wide"
)

# -----------------------------
# Load data
# -----------------------------
# If app.py is in /dashboard, this path assumes you run Streamlit from the repo root:
df = pd.read_csv("data/processed/team_wins_payroll_war_efficiency_2000_2016.csv")

# make sure year is numeric
df["yearID"] = pd.to_numeric(df["yearID"], errors="coerce")

# -----------------------------
# Title / intro
# -----------------------------
st.title("MLB Payroll Efficiency Dashboard")
st.markdown(
    """
Use the sidebar to select teams, a metric, and a year range.  
This dashboard helps explore how payroll, WAR, and wins change over time and how efficiently teams convert payroll into on-field value.
"""
)

# -----------------------------
# Sidebar controls
# -----------------------------
st.sidebar.header("Filters")

teams = st.sidebar.multiselect(
    "Select Teams",
    options=sorted(df["teamID"].dropna().unique()),
    default=["ARI"]
)

metric = st.sidebar.selectbox(
    "Metric",
    options=["W", "Total_WAR", "payroll", "WAR_per_Million"]
)

year_range = st.sidebar.slider(
    "Year Range",
    min_value=int(df["yearID"].min()),
    max_value=int(df["yearID"].max()),
    value=(2000, 2015)
)

# -----------------------------
# Filter data
# -----------------------------
filtered = df[
    (df["teamID"].isin(teams)) &
    (df["yearID"].between(year_range[0], year_range[1]))
].copy()

# Helpful formatting for display
filtered["payroll_millions"] = filtered["payroll"] / 1e6

# -----------------------------
# Main content
# -----------------------------
if not teams:
    st.info("Select at least one team from the sidebar to begin.")
    st.stop()

if filtered.empty:
    st.warning("No data available for the selected filters.")
    st.stop()

# Layout: two columns
left_col, right_col = st.columns([2, 1])

# -----------------------------
# 1) Time series plot (left)
# -----------------------------
with left_col:
    st.subheader("Metric Over Time")

    fig, ax = plt.subplots(figsize=(10, 5))

    # Sort for clean lines
    filtered_sorted = filtered.sort_values(["teamID", "yearID"])

    for team in teams:
        team_df = filtered_sorted[filtered_sorted["teamID"] == team]
        ax.plot(team_df["yearID"], team_df[metric], marker="o", label=team)

    ax.set_xlabel("Season")

    # Better y-axis label for payroll
    if metric == "payroll":
        ax.set_ylabel("Payroll ($M)")
    elif metric == "WAR_per_Million":
        ax.set_ylabel("WAR per $1M Payroll")
    else:
        ax.set_ylabel(metric)

    ax.set_title(f"{metric} by Season")
    ax.legend(title="Team", loc="best")
    plt.tight_layout()

    st.pyplot(fig)

# -----------------------------
# 2) Summary table (right)
# -----------------------------
with right_col:
    st.subheader("Summary (Selected Range)")

    summary = (
        filtered
        .groupby("teamID", as_index=True)
        .agg(
            Seasons=("yearID", "count"),
            Avg_Wins=("W", "mean"),
            Avg_WAR=("Total_WAR", "mean"),
            Avg_Payroll_M=("payroll_millions", "mean"),
            Avg_Efficiency=("WAR_per_Million", "mean"),
        )
        .round(2)
        .sort_values("Avg_Efficiency", ascending=False)
    )

    st.dataframe(summary, use_container_width=True)

# -----------------------------
# 3) Bubble scatter: Payroll vs Wins (below)
# -----------------------------
st.subheader("Payroll vs Wins (Bubble Size = Total WAR)")

fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.scatter(
    filtered["payroll_millions"],
    filtered["W"],
    s=filtered["Total_WAR"].clip(lower=0) * 15,  # scale bubbles; clip avoids negative sizes
    alpha=0.6
)

ax2.set_xlabel("Payroll ($M)")
ax2.set_ylabel("Wins")
ax2.set_title("Payroll vs Wins with WAR as Bubble Size")
plt.tight_layout()

st.pyplot(fig2)

# -----------------------------
# Helpful footer / explainer
# -----------------------------
st.markdown(
    """
**How to read this dashboard**
- The line chart shows year-to-year trends for your selected metric.
- The table summarizes average performance across the selected time window.
- The bubble chart shows payroll vs wins, where larger bubbles represent higher total WAR.
"""
)
