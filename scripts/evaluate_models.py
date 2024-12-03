import logging
from typing import Dict

from sklearn.metrics import classification_report, roc_auc_score

logging.basicConfig(level=logging.INFO, format='%(message)s')

def get_model_evaluations(X_test, y_test, trained_models)->Dict:
    """
    Evaluate all models and return evaluation metrics.
    """
    results = {}
    
    for model_name, model in trained_models.items():
        try:
            y_pred = model.predict(X_test)
            y_prob = model.predict_proba(X_test)[:, 1]  # Ensure this works for your models (binary classification)
            
            report = classification_report(y_test, y_pred, output_dict=True)
            auc_score = roc_auc_score(y_test, y_prob)

            results[model_name] = {
                "classification_report": report,
                "roc_auc_score": auc_score
            }
            
            logging.info(f"Finished {model_name} with AUC: {auc_score:.4f}")
        
        except Exception as e:
            logging.error(f"Error evaluating {model_name}: {e}")
    
    return results
