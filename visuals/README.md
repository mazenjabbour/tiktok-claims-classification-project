# Recruiter-Facing Visuals

This directory contains a lightweight chart-generation script for five portfolio visuals that summarize the TikTok claims-classification project. The script uses only summary values already recorded in the existing notebooks; it does not load the source dataset, modify model code, or retrain a model.

## Generate the visuals locally

From the repository root, install the project requirements and run:

```bash
python visuals/generate_visuals.py
```

The command creates these files locally in `visuals/`:

- `claim_vs_opinion_distribution.png` — shows the nearly balanced labeled target classes.
- `engagement_by_claim_status.png` — contrasts average video views for claims and opinions.
- `champion_model_confusion_matrix.png` — summarizes the Random Forest champion model's held-out test predictions.
- `model_comparison_chart.png` — compares the recorded cross-validated F1 scores for Random Forest and XGBoost.
- `feature_importance_chart.png` — highlights the champion model's reliance on engagement features.

Generated PNGs are intentionally excluded from version control. No PNGs or other binary assets are included in this documentation update.

## Notebook-recorded source values

| Visual | Values used | Existing notebook source |
|---|---|---|
| Claim vs Opinion Distribution | Claim: 9,608; Opinion: 9,476 | `01_data_understanding_and_preparation/notebooks/01_tiktok_data_understanding.ipynb` |
| Engagement by Claim Status | Average views — Claim: 501,029.45; Opinion: 4,956.43 | `01_data_understanding_and_preparation/notebooks/01_tiktok_data_understanding.ipynb` |
| Champion Model Confusion Matrix | Held-out test matrix: `[[1895, 0], [18, 1904]]` | `05_advanced_machine_learning_and_random_forest_modeling/notebooks/05_tiktok_random_forest_classification_pipeline.ipynb` |
| Model Comparison Chart | Random Forest F1: 0.9948518; XGBoost F1: 0.9940670 | `05_advanced_machine_learning_and_random_forest_modeling/notebooks/05_tiktok_random_forest_classification_pipeline.ipynb` |
| Feature Importance Chart | All ten recorded Random Forest feature importances | `05_advanced_machine_learning_and_random_forest_modeling/notebooks/05_tiktok_random_forest_classification_pipeline.ipynb` |

## Interpretation notes

- The labeled classes are almost evenly split, making class imbalance less likely to dominate model evaluation.
- Claim videos average roughly 100 times more views than opinion videos in this fictional dataset.
- The champion model makes very few test-set errors, but its unusually strong performance should still be validated on fresh, production-like data.
- Video views and likes account for most of the champion model's recorded feature importance, reinforcing the need to monitor dependence on engagement signals.
