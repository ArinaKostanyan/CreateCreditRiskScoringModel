import pandas as pd

from sklearn.preprocessing import StandardScaler

from scripts.config import DATA_PATH

class Preprocessing:
    def __init__(self):
        self.data = self.read_data()
        self.scaler = StandardScaler()

    @staticmethod
    def read_data()->pd.DataFrame:
        df = pd.read_excel(DATA_PATH)
        
        # print("Data Overview:")
        # print(df.info())
        # print(df.describe())
        
        return df
        
    def handle_missing_values(self):
        # Fill numeric columns with median
        numeric_cols = ['switch_class_q', 'credit_history_max_overdue', 
                        'max_PMT', 'loan_history_total_overdue', 'current_overdue']
        for col in numeric_cols:
            self.data[col] = self.data[col].fillna(self.data[col].median())

    def feature_engineering(self):
        # Create a binary target variable for default
        self.data['default'] = (self.data['max_overdue'] > 30).astype(float)
        
        # Drop irrelevant columns
        self.data = self.data.drop(columns=['loan_ID', 'start_date', 'max_overdue'])
        
        if 'max_risk_class' in self.data.columns:
            mode_value = self.data[self.data['max_risk_class'] != 'NoNode']['max_risk_class'].mode()[0]
            self.data['max_risk_class'] = self.data['max_risk_class'].replace('NoNode', mode_value)

        if 'received_loans_count' in self.data.columns:
            self.data.loc[self.data['received_loans_count'] == '15a', 'received_loans_count'] = (
                self.data['bank_received_loans_count'] + self.data['uco_received_loans_count']
            )
            self.data['received_loans_count'] = pd.to_numeric(self.data['received_loans_count'], errors='coerce')



        
    def scale_features(self):
        """
        Scale numeric features using StandardScaler.
        """
        numeric_features = self.data.select_dtypes(include=['float64', 'int64']).columns.drop('default', errors='ignore')
        self.data[numeric_features] = self.scaler.fit_transform(self.data[numeric_features])

    def get_processed_data(self)->pd.DataFrame:
        """
        Load and preprocess by cleaning and scaling the data.
        """        
        self.handle_missing_values()
        self.feature_engineering()        
        self.scale_features()
        
        return self.data

    