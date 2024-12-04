import json
from pathlib import Path
import joblib

import pandas as pd
from sklearn.model_selection import train_test_split

from scripts.config import RESULTS_PATH
from scripts.evaluate_models import get_model_evaluations
from scripts.preprocess_data import Preprocessing
from scripts.train_model import get_trained_models


def split_data(data:pd.DataFrame):
    """
    Split data into train and test sets.
    """
    X = data.drop(columns=['default'])
    y = data['default']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    return X_train, X_test, y_train, y_test

def get_best_model(results):
    """
    Get the best model based on the ROC-AUC score.
    """
    best_model = max(results.items(), key=lambda x: x[1]['roc_auc_score'])
    return best_model[0], best_model[1]

def save_results(results, output_path=Path(RESULTS_PATH+"model_results.json")):
    """
    Save evaluation results to a JSON file.
    """
    try:
        with open(output_path, 'w') as f:
            json.dump(results, f, indent=4)
        print(f"Results saved to {output_path}")
    except Exception as e:
        print(f"Error saving results: {e}")

def save_model(model, filename=Path(RESULTS_PATH+"best_model.pkl")):
    """
    Save the trained model to a file.
    """
    joblib.dump(model, filename)
    print(f"Model saved to {filename}")

if __name__ == '__main__':
    preprocessing = Preprocessing()
    # Load and preprocess data
    data = preprocessing.get_processed_data()
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = split_data(data)

    trained_models = get_trained_models(X_train, y_train)
    results = get_model_evaluations(X_test, y_test, trained_models)
    best_model_name, best_model_metrics = get_best_model(results)
    print(f"Best Model: {best_model_name} with AUC: {best_model_metrics['roc_auc_score']:.4f}")

    save_results(results)
    save_model(trained_models[best_model_name])
