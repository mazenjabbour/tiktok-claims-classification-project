# TikTok Claims Classification

An end-to-end data science case study that uses exploratory analysis, statistical testing, and machine learning to distinguish TikTok videos that make **claims** from those that express **opinions**.

## Project Overview

This portfolio project was completed through the Google Advanced Data Analytics Professional Certificate using a fictional TikTok dataset. It demonstrates a complete analytics lifecycle: framing a moderation problem, inspecting and visualizing data, testing hypotheses, engineering features, comparing classification models, and translating results into responsible business recommendations.

## Business Problem

TikTok receives a high volume of user reports that must be reviewed efficiently. A model that identifies whether a video contains a claim or an opinion could help the moderation team prioritize potentially higher-risk content, reduce the review backlog, and allocate human-review capacity more effectively.

The model is intended as a **decision-support and prioritization tool**, not as a replacement for human moderation.

## Dataset Summary

The fictional dataset contains **19,382 TikTok video records** and 12 original variables describing:

- Claim status and video transcription text
- Creator verification and ban status
- Video duration
- Views, likes, shares, downloads, and comments

Of the 19,084 records with a claim-status label, approximately **50.3% are claims** and **49.7% are opinions**, providing a nearly balanced classification target. The source CSV is referenced by the notebooks but is not included in this repository.

## Methodology

1. **Data understanding and preparation:** inspected data types, missing values, class balance, and variable distributions.
2. **Exploratory analysis and visualization:** compared claims and opinions, evaluated outliers, and examined engagement patterns.
3. **Statistical analysis:** tested whether observed differences between relevant groups were statistically meaningful.
4. **Baseline modeling:** used logistic regression to explore factors associated with creator verification status and inform later classification work.
5. **Advanced classification:** engineered transcription-text length, encoded categorical variables, and trained Random Forest and XGBoost models using a 60/20/20 train-validation-test split.
6. **Model selection and interpretation:** tuned hyperparameters with cross-validation, compared classification metrics, selected a champion model, and reviewed feature importance and ethical risks.

## Key Findings

- Claims and opinions are almost evenly represented, reducing the risk of majority-class bias during training.
- Claim videos receive substantially greater engagement; average views were approximately **501,000 for claims** versus **5,000 for opinions**.
- Claim videos are more frequently associated with banned or under-review authors than opinion videos.
- Engagement variables dominate the champion model: video views and likes account for most of its feature importance, followed by comments and shares.
- Creator verification, ban status, video duration, and transcription-text length contribute comparatively little to the final Random Forest model.

## Model Comparison

| Model | Modeling role | Key result | Interpretation |
|---|---|---:|---|
| Logistic Regression | Supporting analysis of verified status | 0.93 accuracy, but 0.00 recall for the minority class | Accuracy was misleading because the model predicted only the majority class. |
| Random Forest | Claim-versus-opinion classifier | Cross-validated F1: **0.9949**; precision: **1.0000** | Best cross-validation performance and selected as the champion model. |
| XGBoost | Claim-versus-opinion classifier | Cross-validated F1: **0.9941**; precision: **0.9991** | Performed nearly as well as Random Forest. |

Both advanced models produced validation precision, recall, and F1 scores that rounded to **0.99–1.00** for each class. Because unusually strong results can indicate leakage, dataset artifacts, or limited real-world complexity, these findings require validation on fresh production-like data before deployment.

## Final Results

The tuned **Random Forest classifier** was selected as the champion model and used to generate predictions on the held-out test set. Its strongest predictors were:

| Feature | Importance |
|---|---:|
| Video view count | 39.77% |
| Video like count | 34.51% |
| Video comment count | 9.80% |
| Video share count | 9.76% |
| Video download count | 5.35% |

The results show that engagement behavior provides a strong signal for separating claims from opinions in this dataset. They also reinforce the need for careful monitoring: engagement can correlate with claim status without proving that content is misleading or harmful.

## Business Recommendations

- Use the model to **rank and prioritize** reported videos for human review rather than automatically removing content.
- Route high-confidence claim predictions with elevated engagement to an expedited moderation queue.
- Add content-based signals such as keywords, sentiment, embeddings, hashtags, audio, and report history to reduce dependence on engagement metrics.
- Validate performance on recent, production-like data and monitor precision, recall, drift, and subgroup outcomes after launch.
- Establish reviewer feedback loops so moderation decisions can improve future model versions.

## Limitations and Ethical Considerations

- The dataset is fictional and may not represent real TikTok behavior, language, creators, or moderation outcomes.
- The source dataset is not stored in this repository, which limits full out-of-the-box reproducibility.
- High validation performance may reflect strong dataset-specific patterns and should not be assumed to generalize.
- Engagement-based predictions may amplify popularity effects and disproportionately flag viral content.
- A claim is not necessarily false, harmful, or policy-violating; automated classification must not be treated as a factuality judgment.
- Human oversight, bias testing, explainability, appeals, privacy safeguards, and ongoing monitoring are essential for responsible use.

## Repository Structure

```text
.
├── 01_data_understanding_and_preparation/                 # Initial inspection and planning
├── 02_exploratory_data_analysis_and_visual_storytelling/ # EDA, visuals, and Tableau work
├── 03_statistical_analysis_and_hypothesis_testing/        # Statistical testing and summary
├── 04_machine_learning_classification_modeling/           # Logistic regression analysis
├── 05_advanced_machine_learning_and_random_forest_modeling/ # Random Forest and XGBoost
├── 06_end_to_end_data_science_capstone_project/           # Separate employee-attrition capstone
├── requirements.txt                                       # Python dependencies
└── README.md                                              # Project case study
```

Each project folder contains a focused combination of notebooks, planning documents, reports, or supporting visuals.

## Technologies Used

- **Languages and environments:** Python, Jupyter Notebook
- **Data analysis:** pandas, NumPy, SciPy
- **Visualization:** Matplotlib, seaborn, Tableau Public
- **Machine learning:** scikit-learn, XGBoost, GridSearchCV
- **Model evaluation:** confusion matrices, precision, recall, F1 score, accuracy, and feature importance
- **Version control:** Git and GitHub

## Reproducibility Instructions

1. Clone the repository and enter the project directory:
   ```bash
   git clone <repository-url>
   cd tiktok-claims-classification-project
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Obtain the fictional `tiktok_dataset.csv` used in the Google Advanced Data Analytics certificate labs and place it in the working directory expected by each TikTok notebook.
5. Launch Jupyter and run the TikTok notebooks in numbered order:
   ```bash
   jupyter notebook
   ```

## Author

**Mazen Jabbour**

Senior Data Analyst | Statistician | Data Science & Business Intelligence Enthusiast

Founder of OrcaStat

- [GitHub](https://github.com/mazenjabbour)
- [Maven Showcase Portfolio](https://mavenshowcase.com/profile/e8012350-2051-70f4-2885-003ee8ad3bf1)
