# Data Setup

The source datasets are intentionally **not included** in this repository. They were supplied through the Google Advanced Data Analytics Professional Certificate labs and must be obtained from an authorized source before the notebooks can be executed from raw data.

## Expected files and canonical location

Place the datasets in this directory using the exact filenames below:

```text
data/
├── tiktok_dataset.csv
└── HR_capstone_dataset.csv
```

| Dataset | Used by | Expected rows | Description |
|---|---|---:|---|
| `tiktok_dataset.csv` | TikTok notebooks in project stages 01, 02, 04, and 05 | 19,382 | Fictional TikTok video-level data used to analyze and classify claims versus opinions. |
| `HR_capstone_dataset.csv` | Salifort Motors notebook in project stage 06 | 14,999 | Fictional employee-level HR data used to analyze and predict employee turnover. |

The stage 03 statistical-analysis notebook currently contains imports only and does not load a dataset or implement the reported hypothesis test.

## Expected columns

### `tiktok_dataset.csv`

The file is expected to contain these 12 columns, preserving spelling and capitalization:

| Column | Description |
|---|---|
| `#` | Source row identifier. |
| `claim_status` | Target label indicating whether a video is a `claim` or `opinion`; some rows are missing labels. |
| `video_id` | Unique video identifier. |
| `video_duration_sec` | Video duration in seconds. |
| `video_transcription_text` | Video transcription text; some rows are missing text. |
| `verified_status` | Whether the author is verified. |
| `author_ban_status` | Author account status, such as active, under review, or banned. |
| `video_view_count` | Number of video views. |
| `video_like_count` | Number of video likes. |
| `video_share_count` | Number of video shares. |
| `video_download_count` | Number of video downloads. |
| `video_comment_count` | Number of video comments. |

### `HR_capstone_dataset.csv`

The source file is expected to contain these 10 columns. Note that `average_montly_hours` is intentionally spelled as it appears in the source CSV; the notebook renames it after loading.

| Column | Description |
|---|---|
| `satisfaction_level` | Employee-reported satisfaction score. |
| `last_evaluation` | Most recent performance-evaluation score. |
| `number_project` | Number of projects assigned to the employee. |
| `average_montly_hours` | Average monthly hours worked (source-file spelling). |
| `time_spend_company` | Employee tenure in years. |
| `Work_accident` | Indicator that the employee experienced a workplace accident. |
| `left` | Target indicator that the employee left the company. |
| `promotion_last_5years` | Indicator that the employee was promoted in the previous five years. |
| `Department` | Employee department. |
| `salary` | Salary-band category. |

## Notebook path compatibility

The existing notebooks must remain unchanged and load their CSVs with bare filenames such as `pd.read_csv("tiktok_dataset.csv")`. Before running a notebook interactively, copy the appropriate file from this canonical `data/` directory into that notebook's directory. For example:

```bash
cp data/tiktok_dataset.csv 01_data_understanding_and_preparation/notebooks/
cp data/HR_capstone_dataset.csv 06_end_to_end_data_science_capstone_project/notebooks/
```

Repeat the TikTok copy for stages 02, 04, and 05 as needed. CSV files are ignored by Git so these local compatibility copies will not be committed.

## Missing dataset and licensing notice

If either CSV is absent, the associated notebook will raise `FileNotFoundError`; this is expected because the repository does not distribute the lab datasets. Dataset ownership, licensing, and redistribution permissions remain with the original provider. Obtain the files through the course/lab or another authorized source, review the applicable terms, and do not commit or redistribute them through this repository.
