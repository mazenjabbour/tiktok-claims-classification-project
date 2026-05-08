# Course 4 PACE Strategy Document — Filled Summary

## Plan
The stakeholders include TikTok leadership, the data science team, project management officers, and business stakeholders interested in improving content moderation and classification workflows.

The project aims to build a logistic regression model that supports classification-related analysis using TikTok video data.

Initial EDA showed that engagement variables such as views, likes, shares, comments, and downloads are highly skewed. Some videos receive extremely high engagement, which is common in social media data.

## Analyze
EDA helps identify missing values, duplicates, outliers, class imbalance, variable distributions, and relationships between predictors and the outcome variable.

An ethical consideration is that model outputs may influence moderation-related decisions, so results should support human review rather than replace it.

## Construct
A logistic regression model was constructed using selected TikTok video and account features.

Some variables are highly correlated and engagement metrics are heavily skewed. The model could be improved by testing additional algorithms, applying transformations, and improving feature engineering.

## Execute
The logistic regression model provides a structured way to estimate the probability of the selected outcome based on video and account characteristics.

Beta coefficients are important because they show how each predictor affects the log-odds of the modeled outcome.

Business recommendations:
- Use the model as a decision-support tool.
- Continue improving feature engineering.
- Evaluate performance carefully using classification metrics.
- Review fairness and bias before operational use.
