# TikTok Claims Classification Project

![Python](https://img.shields.io/badge/Python-Data%20Analysis-blue)
![Pandas](https://img.shields.io/badge/Pandas-EDA-150458)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-4c72b0)
![Tableau](https://img.shields.io/badge/Tableau-Public-orange)
![Portfolio](https://img.shields.io/badge/Portfolio-Project-success)

## Overview

This project analyzes TikTok video data to distinguish between **claim-based content** and **opinion-based content**, with the goal of supporting **content moderation and predictive modeling**.

The analysis focuses on understanding **engagement patterns (views, likes, shares, comments)** and how they relate to potentially risky or viral content.

---

## Objectives

* Perform Exploratory Data Analysis (EDA)
* Identify key differences between claim and opinion videos
* Detect patterns in user engagement behavior
* Prepare data for future machine learning classification

---

## Dataset

* ~19,000 TikTok videos
* Key features:

  * video_view_count
  * video_like_count
  * video_comment_count
  * video_share_count
  * video_download_count
  * claim_status
  * author_ban_status
  * verified_status

---

## Repository Structure

```text
tiktok-claims-classification-project/
├── course1/
│   ├── docs/
│   ├── notebooks/
│   └── reports/
├── course2/
│   ├── docs/
│   ├── notebooks/
│   ├── reports/
│   └── tableau/
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Course 1 — Data Understanding

Focused on:

* Dataset inspection
* Project proposal
* Initial assumptions
* PACE strategy

Deliverables:

* Project proposal
* PACE document
* Data inspection notebook
* Executive summary

---

## Course 2 — Exploratory Data Analysis (EDA)

Focused on:

* Data cleaning and validation
* Distribution analysis
* Outlier detection
* Engagement analysis
* Visualization (Python + Tableau)

Deliverables:

* EDA notebook
* PACE strategy document
* Executive summary
* Tableau dashboard

---

## Key Insights

* **Claim videos dominate engagement**, generating ~99% of total views
* Engagement variables are **highly right-skewed**, reflecting viral content behavior
* A **small number of videos drive the majority of engagement**
* **Non-active users (banned / under review)** have significantly higher median views
* **Verified users tend to post opinions**, while unverified users contribute more claims

---

## Visualizations

* Scatter plot (views vs likes)
* Boxplots for engagement variables
* Distribution histograms
* Author status comparisons
* Tableau dashboard

---

## Tableau Dashboard

https://public.tableau.com/views/Tiktokfictionaldata/Sheet1

---

## Tools Used

* Python (Pandas, NumPy)
* Seaborn & Matplotlib
* Tableau Public

---

## Business Impact

* Helps prioritize **high-risk viral content** for moderation
* Identifies **engagement-driven signals of claim content**
* Supports development of **predictive classification models**

---

## Portfolio Value

This project demonstrates:

* Data cleaning & preprocessing
* Exploratory Data Analysis (EDA)
* Outlier reasoning
* Data visualization
* Business-focused interpretation
* Communication of insights
* Tableau integration

---

## Next Steps

* Build classification model (Course 3)
* Feature engineering
* Model evaluation
* Predictive deployment

---

## Author

Mazen Jabbour
Senior Data Analyst | Data Science Portfolio

