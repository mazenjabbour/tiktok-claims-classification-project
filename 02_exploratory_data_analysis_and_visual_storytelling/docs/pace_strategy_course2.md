# Course 2 PACE Strategy Document — TikTok Claims Classification Project

## Plan
**Relevant variables**
- `claim_status`
- `video_view_count`
- `video_like_count`
- `video_comment_count`
- `video_share_count`
- `video_download_count`
- `video_duration_sec`
- `verified_status`
- `author_ban_status`

**Units**
- Engagement variables are counts.
- `video_duration_sec` is measured in seconds.

**Initial assumptions**
- Claim videos are likely to generate higher engagement than opinion videos.
- Highly viral content may be more strongly associated with claims and non-active accounts.
- Engagement variables will likely be right-skewed due to a small number of viral videos.

**Missing / incomplete data**
- Some records contain missing values in key engagement or text fields and require inspection before analysis.

**Formatting / data type checks**
- Confirm numeric columns are numeric.
- Check whether missing values and duplicates affect analysis.

**EDA practices required**
- Summary statistics
- Missing value inspection
- Outlier detection
- Distribution plots
- Group comparisons by claim status, verification status, and author ban status

## Analyze
**Steps for effective EDA**
1. Load and inspect the dataset
2. Review data types and missing values
3. Visualize numerical distributions
4. Detect outliers with boxplots and IQR-based reasoning
5. Compare claim vs opinion groups
6. Evaluate verification status and author ban status relationships
7. Explore relationships among engagement variables

**Structuring needs**
- Filtering by claim status where useful
- Grouping by claim status / verification / author ban status
- Summarizing medians and totals for engagement variables

**Visualization assumptions**
- Bar charts are best for category counts
- Boxplots are best for outlier detection
- Histograms are best for distributions
- Scatter plots are best for relationships between engagement variables

## Construct
**Outputs to build**
- Python EDA notebook
- Matplotlib / seaborn visualizations
- Tableau scatter plot / dashboard support
- Executive summary

**Processes to build visuals**
- Aggregate category counts
- Group median / total engagement values
- Plot distributions and relationships with clear labeling and accessible styling

**Most applicable variables**
- `claim_status`
- `video_view_count`
- `video_like_count`
- `video_comment_count`
- `video_share_count`
- `video_download_count`
- `author_ban_status`
- `verified_status`

**Missing data approach**
- Inspect missingness first
- Keep valid observations whenever possible
- Avoid removing meaningful viral examples unless they are clearly erroneous

## Execute
**Key insights**
- Claim videos dominate total views and engagement.
- Engagement variables are heavily right-skewed.
- Non-active authors have much higher median view counts than active authors.
- Verified users are relatively rare and appear more likely to post opinions than claims.

**Business recommendations**
- Use engagement variables as important predictors in later modeling.
- Prioritize high-view / high-share claim content for moderation review.
- Handle outliers carefully rather than removing them blindly because viral content is business-relevant.

**Additional questions**
- Which engagement variable is the strongest predictor of claim status?
- Are there useful thresholds for prioritizing moderation?
- How do verified and unverified users differ across all engagement metrics?

**Audience sharing**
- Technical audience: full notebook + deeper metrics
- Management / stakeholders: concise executive summary + Tableau visualization
