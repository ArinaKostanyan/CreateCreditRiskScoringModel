from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier

from scripts.config import MODELS_CONFIG


def get_model_class(model_name):
    """
    Return the model class based on the model name.
    """
    if model_name == "LogisticRegression":
        return LogisticRegression
    elif model_name == "RandomForestClassifier":
        return RandomForestClassifier
    elif model_name == "XGBoost":
        return XGBClassifier
    else:
        raise ValueError(f"Model '{model_name}' is not recognized.")

def train_single_model(model_name, params, X_train, y_train):
    """
    Train a single model using the provided parameters.
    """
    model_class = get_model_class(model_name)
    model = model_class(**params)
    model.fit(X_train, y_train)
    return model

def get_trained_models(X_train, y_train):
    """
    Train all models from the configuration and return them in a dictionary.
    """
    trained_models = {}
    for model_config in MODELS_CONFIG:
        model_name = model_config['name']
        model_params = model_config['params']
        print(f"Training {model_name}...")
        trained_model = train_single_model(model_name, model_params, X_train, y_train)
        trained_models[model_name] = trained_model
        
    return trained_models

