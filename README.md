MLB Team Construction & Win Efficiency Analysis
Project Overview

This project analyzes how Major League Baseball teams convert payroll into on-field success, with a focus on Wins Above Replacement (WAR) as the key mediating variable between spending and wins.

Rather than treating payroll as a direct predictor of team success, the analysis evaluates organizational efficiency — identifying which teams consistently generate more on-field value per dollar spent and which experience diminishing returns despite high payrolls.

The project is structured as a multi-notebook analytical pipeline, progressing from data ingestion and feature engineering to exploratory analysis and, ultimately, statistical modeling.

Key Questions

How strongly are payroll and wins related across MLB teams?

Does WAR explain variation in wins more effectively than payroll alone?

Which teams consistently generate the most and least WAR per dollar spent?

How does payroll efficiency shape competitive outcomes across seasons?

To what extent does WAR mediate the relationship between payroll and wins?

Data Sources

Lahman Baseball Database (SQL)

Team-level wins, payroll, and franchise identifiers

Historical WAR dataset (player-level)

Aggregated to team-season WAR totals

Timeframe: 2000–2016 (limited by payroll data availability)

All data processing and joins are handled locally using SQL and Python.

Project Structure
MLB-Team-Construction---Win-Efficiency/
│
├── notebooks/
│   ├── 01_data_ingestion_feature_engineering.ipynb
│   ├── 02_team_efficiency_analysis.ipynb
│   ├── 03_modeling.ipynb              
│   └── 04_visual_storytelling.ipynb   # (planned)
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── visuals/
│   ├── avg_cost_per_war_line.png
│   ├── best_value_bar.png
│   ├── cost_per_war_bar.png
│   └── payroll_vs_war_bubble.png
│   └── payroll_vs_wins.png
│   └── payroll_vs_wins_war_scatter.png
│   └── War_vs_Wins_bubble.png
│   └── worst_value_teams.png
│   └── model_actual_vs_pred.png
│   └── model_residuals.png
│
├── requirements.txt
└── README.md

Notebook Summaries
Notebook 1: Data Ingestion & Feature Engineering

This notebook builds the analytical foundation of the project.

Key steps:

Loaded team wins, payroll, and WAR data from SQL sources

Aggregated player-level WAR to team-season totals

Engineered efficiency metrics, including:

WAR per $1M payroll

Dollars per WAR

Wins above WAR-based expectations

Validated data integrity using assertion checks

Exported a clean, processed dataset for downstream analysis

Notebook 2: Team Efficiency Analysis

This notebook explores how teams translate payroll into wins through WAR.

Analytical highlights:

Examined relationships between:

Payroll and wins

WAR and wins

Payroll and WAR

Introduced WAR as a mediating variable using a bubble plot visualization

Defined and analyzed payroll efficiency metrics

Ranked teams by median WAR per dollar spent:

Best Value Teams: Consistently high WAR efficiency

Worst Value Teams: Persistent diminishing returns on payroll

Added league median benchmarks to contextualize efficiency rankings

Synthesized findings to show that payroll impacts wins primarily through its ability to generate WAR

Notebook 3: Statistical Modeling

This notebook formalizes earlier findings using interpretable regression models.

Modeling approach:

Baseline model using payroll alone

WAR-only model

Combined payroll and WAR model

Extended model separating batting and pitching WAR

Key modeling results:

Payroll alone explains little variation in wins

WAR explains the majority of variation in team wins

Including payroll alongside WAR provides minimal additional explanatory power

Separating WAR into batting and pitching components yields the strongest predictive performance

Model diagnostics indicate good calibration, stable residual variance, and strong generalization to unseen data

These results confirm that payroll influences wins primarily through its ability to generate on-field value.

Notebook 4: Visual Storytelling and Executive Summary

This notebook translates analytical findings into an executive-facing narrative.

Focus areas:

High-level framing of payroll versus wins

Visual demonstration of WAR as the key driver of success

Clear presentation of best and worst value teams

Simplified model results without technical detail

Actionable takeaways for front office decision-making

This notebook is designed to be read independently by non-technical stakeholders.

Key Insights

Payroll alone is an inconsistent predictor of team success

WAR explains team wins far more effectively than spending

Teams with similar payrolls can achieve vastly different outcomes based on efficiency

Several small- and mid-market teams consistently outperform financial expectations

High payrolls often exhibit diminishing returns absent efficient roster construction

Pitching WAR shows a slightly stronger marginal impact on wins than batting WAR

Visual Outputs

All major plots are saved to the visuals/ directory, including:

Payroll vs Wins

Payroll vs Wins with WAR as bubble size

Best Value Teams by payroll efficiency

Worst Value Teams by payroll efficiency

Model diagnostics including actual vs predicted wins and residuals

This allows the analysis to be reviewed without executing notebooks.

Tools & Technologies

Python: pandas, numpy, matplotlib

SQL: SQLite

Modeling: statsmodels, scikit-learn

Environment: Jupyter Notebooks

Conclusion

This project demonstrates that competitive success in Major League Baseball depends less on how much teams spend and more on how effectively they convert spending into on-field value.

Organizations that prioritize WAR efficiency consistently outperform financial expectations, while high payrolls alone do not guarantee success.

Author

Matthew Edelson
Data Analytics | Sports Analytics | Machine Learning