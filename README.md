# TikTok Claims Classification Project

![Python](https://img.shields.io/badge/Python-Data%20Analysis-blue)
![Pandas](https://img.shields.io/badge/Pandas-EDA-150458)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-4c72b0)
![Tableau](https://img.shields.io/badge/Tableau-Public-orange)
![Statistics](https://img.shields.io/badge/Statistics-Hypothesis%20Testing-red)
![Portfolio](https://img.shields.io/badge/Portfolio-Project-success)

---

## Overview

This project analyzes TikTok video data to distinguish between **claim-based content** and **opinion-based content**, with the goal of supporting **content moderation, engagement analysis, and predictive modeling**.

The project follows a full analytics workflow:

* Data understanding
* Exploratory Data Analysis (EDA)
* Statistical testing
* (Next: Machine Learning modeling)

---

## Objectives

* Understand the structure and quality of the dataset
* Identify patterns in user engagement
* Compare claim vs opinion content
* Evaluate the impact of verification status on video performance
* Prepare data for predictive modeling

---

## Dataset

* ~19,000 TikTok videos
* Key variables:

  * video_view_count
  * video_like_count
  * video_comment_count
  * video_share_count
  * video_download_count
  * claim_status
  * verified_status
  * author_ban_status

---

## Repository Structure

```text
tiktok-claims-classification-project/
├── course1/
├── course2/
├── course3/
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Course 1 — Data Understanding

**Focus:**

* Dataset inspection
* Project proposal
* Initial assumptions
* PACE strategy

**Deliverables:**

* Data inspection notebook
* Project proposal
* Executive summary
* PACE document

---

## Course 2 — Exploratory Data Analysis (EDA)

**Focus:**

* Data cleaning and validation
* Distribution analysis
* Outlier detection
* Engagement analysis
* Visualization (Python + Tableau)

**Key Insights:**

* Claim videos generate ~99% of total views
* Engagement metrics are highly skewed (viral distribution)
* A small number of videos drive most engagement

**Deliverables:**

* EDA notebook
* Tableau dashboard
* Executive summary

---

## Course 3 — Statistical Analysis & Hypothesis Testing

**Focus:**

* Descriptive statistics
* Hypothesis testing
* Statistical inference

**Research Question:**

> Is there a statistically significant difference in video view counts between verified and unverified accounts?

**Method Used:**

* Two-sample t-test (Welch’s t-test)
* Significance level: α = 0.05

**Hypotheses:**

* H₀: μ_verified = μ_unverified
* H₁: μ_verified ≠ μ_unverified

**Key Result:**

* p-value ≈ 0.000 (extremely small)
* Strong evidence to reject the null hypothesis

**Insight:**

* Verification status significantly impacts video view counts
* Engagement differs between verified and unverified users

**Business Impact:**

* Verification status can be used as a predictive feature
* Helps prioritize high-impact content for moderation
* Supports engagement-based classification models

**Deliverables:**

* Hypothesis testing notebook
* PACE strategy document
* Executive summary

---

## Tableau Dashboard

https://public.tableau.com/views/Tiktokfictionaldata/Sheet1

---

## Tools Used

* Python (Pandas, NumPy)
* Seaborn & Matplotlib
* SciPy (statistical testing)
* Tableau Public

---

## Portfolio Value

This project demonstrates:

* Data cleaning & preprocessing
* Exploratory Data Analysis (EDA)
* Statistical reasoning & hypothesis testing
* Data visualization
* Business-focused interpretation
* Communication of insights

---

## Next Steps

* Build classification model (Course 4)
* Feature engineering
* Model evaluation
* Predictive analytics deployment

---

## Author

Mazen Jabbour
Senior Data Analyst | Data Science Portfolio


