# Executive Summary — Course 2 TikTok Claims Classification Project

## Overview
This analysis explored TikTok videos to understand differences between **claim** and **opinion** content. The goal was to support future model development for classifying potentially risky content while helping stakeholders better understand engagement patterns.

## What was done
- Performed exploratory data analysis (EDA)
- Reviewed missingness and variable distributions
- Examined outliers with boxplots and histograms
- Compared claim and opinion videos across engagement metrics
- Assessed relationships with verification status and author ban status
- Built Python visualizations and prepared Tableau-ready outputs

## Key findings
- **Claim videos dominate engagement**, accounting for the overwhelming majority of total views.
- Engagement variables such as views, likes, comments, shares, and downloads are **highly right-skewed**.
- A **small number of viral videos** generate a disproportionately large share of engagement.
- **Banned and under-review authors** have much higher median view counts than active authors.
- **Verified accounts are far fewer** and appear more likely to post opinions than claims.

## Outlier assessment
Outliers are substantial across all engagement variables, but they appear to reflect the real nature of viral social media content rather than obvious data-entry errors. Because of this, outliers should not simply be deleted.

## Proposed solution for outliers
For modeling, use one or more of the following:
- log transformation of engagement variables
- winsorization / capping at high percentiles
- robust modeling methods less sensitive to extreme values

These approaches retain business-relevant viral content while reducing distortion in predictive models.

## Business impact
The analysis suggests that engagement metrics—especially views and likes—are likely to be important indicators of claim status. This supports a moderation workflow where highly viral content is prioritized for review.

## Next steps
- Build classification models in later course work
- Test feature importance for engagement metrics
- Compare model performance with and without transformed engagement variables
- Expand Tableau dashboard for stakeholder monitoring
