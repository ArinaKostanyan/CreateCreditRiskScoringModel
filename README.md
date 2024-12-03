# Credit Risk Scoring Model

This project aims to build a scoring model for making lending decisions based on historical loan data.
The model predicts whether a customer is likely to default on their loan. 
The project involves data preprocessing, model training, evaluation, and selection
of the best-performing model based on ROC-AUC scores.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Technologies Used](#technologies-used)
3. [Installation and Setup](#installation-and-setup)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Results](#results)
7. [License](#license)

---

## Introduction

This project includes:

- **Data Preprocessing**: Handles missing values, encodes categorical variables, and scales numerical features.
- **Model Training**: Includes Logistic Regression, Random Forest, and XGBoost classifiers.
- **Performance Metrics**: Evaluates models using metrics such as ROC-AUC, F1-score, precision, and recall.

---

## Technologies Used

- Python (>= 3.10)
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- JSON for results storage

---

## Installation and Setup

### Prerequisites

- Python 3.10 or later.
- For Mac users, `brew` for managing packages (used to install `libomp` for XGBoost compatibility).

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/ArinaKostanyan/CreateCreditRiskScoringModel.git
   cd CreateCreditRiskScoringModel 
2. Create and activate a virtual environment: 
   ```bash
    python3 -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate     # On Windows
3. Install the required dependencies:
   ```bash
    pip install -r requirements.txt
    (Mac users) If you encounter issues with XGBoost, install libomp:
    brew install libomp

## Usage

### Run the Model

1. Activate the virtual environment:
    ```bash
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
2. Prepare the dataset:
    Place your dataset file (e.g., Data.xlsx) in the data/ directory in the excel format.
3. Run the main script:
   ```bash
    python main.py
4. Review the output(result):


## Project Structure
```
.
├── data/                     # Contains the input data
├── scripts/
│   ├── preprocess_data.py    # Data preprocessing pipeline
│   ├── train_model.py        # Model training logic
│   ├── evaluate_models.py    # Model evaluation
│   ├── config.py             # Configuration for model 
├── main.py                   # Entry point to run the project
├── requirements.txt          # Python dependencies
├── README.md                 # Documentation
└── model_results.json        # Saved evaluation results
```
## Results

After running the script, the output will include:

- The best performing model.
- Metrics such as ROC-AUC, precision, recall, and F1-score.
- A detailed classification report for each model, saved in model_results.json.
