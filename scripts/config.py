DATA_PATH = "data/Data.xlsx"  # Path to the input data file

LOGISTIC_REGRESSION_PARAMS = {
    "C": 1.0,          # Regularization strength
    "max_iter": 100,   # Maximum number of iterations for optimization
    "solver": "lbfgs"  # Solver to use for optimization
}

RANDOM_FOREST_PARAMS = {
    "n_estimators": 100,   # Number of trees in the forest
    "max_depth": None,     # Maximum depth of the trees
    "random_state": 42     # Random state for reproducibility
}

XGBOOST_PARAMS = {
    "learning_rate": 0.1,  # Step size shrinking to prevent overfitting
    "n_estimators": 100,   # Number of boosting rounds (trees)
    "max_depth": 6,        # Maximum depth of individual trees
    "random_state": 42     # Random state for reproducibility
}

MODELS_CONFIG = [
    {"name": "LogisticRegression", "params": LOGISTIC_REGRESSION_PARAMS},
    {"name": "RandomForestClassifier", "params": RANDOM_FOREST_PARAMS},
    {"name": "XGBoost", "params": XGBOOST_PARAMS},
]

