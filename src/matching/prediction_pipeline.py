import joblib
import pandas as pd
from pathlib import Path
from src.features.feature_engineering import (create_pairwise_features)


class CompatibilityPredictor: 

    def __init__(self):

          project_root = Path(__file__).resolve().parents[2]
          model_dir = project_root / "models"

          self.model = joblib.load(
            model_dir / "final_xgboost_model.pkl"
          )

          self.label_encoder = joblib.load(
            model_dir / "label_encoder.pkl"
        )

          self.selected_features = joblib.load(
            model_dir / "selected_features.pkl"
        )

          print("✅ Model Loaded Successfully!")

    
    # Creatng Feature Preparation

    def prepare_features(self, student_1, student_2):
        
        df = create_pairwise_features(student_1, student_2)
        
        return df

    # Creating Column Alignment

    def align_columns(self, df):

        df = pd.get_dummies(
            df, 
            drop_first=False
            )

        for column in self.selected_features:

            if column not in df.columns:
              df[column] = 0

        df = df[self.selected_features]

        return df

    # Create Prediction Function

    def predict(self, student_1, student_2):
        
        df = self.prepare_features(student_1, student_2)

        df = self.align_columns(df)

        prediction = self.model.predict(df)[0]

        probabilities = self.model.predict_proba(df)[0]

        label = self.label_encoder.inverse_transform([prediction])[0]

        confidence = float(probabilities.max())

        return {
            "compatibility_label": label,

            "compatibility_score": round(
                confidence * 100,
                2
            ),

            "probabilities": {

                class_name: round(
                    float(prob),
                    4
                ) 

                for class_name, prob in zip(
                    self.label_encoder.classes_,
                    probabilities
                )
            }
        }


if __name__ == "__main__":

    predictor = CompatibilityPredictor()

    student_1 = {

        "sleep_time": 23,
        "wake_time": 7,
        "gaming_hours": 2,
        "cleanliness_score": 4,
        "privacy_preference": 4,
        "noise_sleep_tolerance": 3,
        "lifestyle_type": "introvert"
    }

    student_2 = {

        "sleep_time": 22,
        "wake_time": 6,
        "gaming_hours": 1,
        "cleanliness_score": 4,
        "privacy_preference": 4,
        "noise_sleep_tolerance": 3,
        "lifestyle_type": "introvert"
    }

    result = predictor.predict(
        student_1,
        student_2
    )

    print(result)