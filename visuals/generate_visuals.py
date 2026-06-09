"""Generate recruiter-facing charts from values recorded in project notebooks.

This script intentionally uses static, notebook-recorded summary values so it does
not require the source dataset, load model artifacts, or retrain a model.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


OUTPUT_DIR = Path(__file__).resolve().parent
COLORS = {"Claim": "#25F4EE", "Opinion": "#FE2C55"}

# Values recorded in the existing TikTok project notebooks.
CLAIM_STATUS_COUNTS = {"Claim": 9608, "Opinion": 9476}
MEAN_VIEWS = {"Claim": 501029.4527477102, "Opinion": 4956.43224989447}
CHAMPION_TEST_CONFUSION_MATRIX = np.array([[1895, 0], [18, 1904]])
MODEL_F1_SCORES = {"Random Forest": 0.9948517564360305, "XGBoost": 0.9940670353790725}
FEATURE_IMPORTANCES = {
    "Video view count": 0.397723,
    "Video like count": 0.345131,
    "Video comment count": 0.098033,
    "Video share count": 0.097620,
    "Video download count": 0.053479,
    "Text length": 0.005929,
    "Author banned": 0.001356,
    "Verified author": 0.000344,
    "Video duration": 0.000270,
    "Author under review": 0.000114,
}


def style_chart() -> None:
    """Apply a consistent, portfolio-ready chart style."""
    sns.set_theme(style="whitegrid", context="talk")
    plt.rcParams.update({"figure.dpi": 120, "savefig.dpi": 200, "axes.titleweight": "bold"})


def save_chart(filename: str) -> None:
    """Save the current chart and close its figure."""
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / filename, bbox_inches="tight", facecolor="white")
    plt.close()


def claim_vs_opinion_distribution() -> None:
    labels, values = zip(*CLAIM_STATUS_COUNTS.items())
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(labels, values, color=[COLORS[label] for label in labels])
    ax.bar_label(bars, labels=[f"{value:,}" for value in values], padding=5)
    ax.set(title="Claim vs Opinion Distribution", ylabel="Labeled videos", ylim=(0, 11000))
    ax.spines[["top", "right"]].set_visible(False)
    save_chart("claim_vs_opinion_distribution.png")


def engagement_by_claim_status() -> None:
    labels, values = zip(*MEAN_VIEWS.items())
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(labels, values, color=[COLORS[label] for label in labels])
    ax.bar_label(bars, labels=[f"{value:,.0f}" for value in values], padding=5)
    ax.set(title="Engagement by Claim Status", ylabel="Average video views")
    ax.ticklabel_format(axis="y", style="plain")
    ax.spines[["top", "right"]].set_visible(False)
    save_chart("engagement_by_claim_status.png")


def champion_model_confusion_matrix() -> None:
    fig, ax = plt.subplots(figsize=(7, 6))
    sns.heatmap(
        CHAMPION_TEST_CONFUSION_MATRIX,
        annot=True,
        fmt=",d",
        cmap="Blues",
        cbar=False,
        xticklabels=["Opinion", "Claim"],
        yticklabels=["Opinion", "Claim"],
        ax=ax,
    )
    ax.set(title="Champion Model Confusion Matrix", xlabel="Predicted label", ylabel="Actual label")
    save_chart("champion_model_confusion_matrix.png")


def model_comparison_chart() -> None:
    labels, values = zip(*MODEL_F1_SCORES.items())
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(labels, values, color=["#111111", "#FE2C55"])
    ax.bar_label(bars, labels=[f"{value:.4f}" for value in values], padding=5)
    ax.set(title="Model Comparison Chart", ylabel="Cross-validated F1 score", ylim=(0.98, 1.0))
    ax.spines[["top", "right"]].set_visible(False)
    save_chart("model_comparison_chart.png")


def feature_importance_chart() -> None:
    labels = list(FEATURE_IMPORTANCES.keys())[::-1]
    values = [FEATURE_IMPORTANCES[label] for label in labels]
    fig, ax = plt.subplots(figsize=(10, 7))
    bars = ax.barh(labels, values, color="#25F4EE")
    ax.bar_label(bars, labels=[f"{value:.1%}" for value in values], padding=4, fontsize=10)
    ax.set(title="Feature Importance Chart", xlabel="Random Forest feature importance", xlim=(0, 0.45))
    ax.spines[["top", "right"]].set_visible(False)
    save_chart("feature_importance_chart.png")


def main() -> None:
    """Generate all five portfolio visuals in the visuals directory."""
    style_chart()
    claim_vs_opinion_distribution()
    engagement_by_claim_status()
    champion_model_confusion_matrix()
    model_comparison_chart()
    feature_importance_chart()
    print(f"Generated five visuals in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
