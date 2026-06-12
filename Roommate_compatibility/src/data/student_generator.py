import pandas as pd


import random
from pathlib import Path

import numpy as np
import pandas as pd

from src.data.distributions import(
    generate_lifestyle_type
)

from src.data.profile_generators import (
    generate_demographic_features,
    generate_sleep_features,
    generate_study_features,
    generate_cleanliness_features,
    generate_social_features,
    generate_privacy_features,
    generate_environment_features,
    generate_personality_features,
    generate_lifestyle_features,
    generate_financial_features
)

class StudentGenerator:

    """
    Main orchestration engine for synthetic
    roommate compatibility dataset generation.
    """

    def __init__(self, seed: int =42):

        self.seed = 42

        random.seed(seed)
        np.random.seed(seed)

    # =====================================================
    # GENERATE SINGLE STUDENT
    # =====================================================

    def generate_student(self, student_id: int):

        student = {

            "student_id": student_id
        }

        # -------------------------------------------------
        # Lifestyle Archetype
        # -------------------------------------------------

        lifestyle_type = generate_lifestyle_type()

        student["lifestyle_type"] = lifestyle_type  # student dictionary

        # -------------------------------------------------
        # Demographics
        # -------------------------------------------------

        student.update(
            generate_demographic_features()
        )

        # -------------------------------------------------
        # Sleep Features
        # -------------------------------------------------

        student.update(
            generate_sleep_features(
                lifestyle_type
            )
        )

        # -------------------------------------------------
        # Study Features
        # -------------------------------------------------

        student.update(
            generate_study_features(
                lifestyle_type
            )
        )

        # -------------------------------------------------
        # Cleanliness Features
        # -------------------------------------------------

        student.update(
            generate_cleanliness_features(
                lifestyle_type
            )
        )

        # -------------------------------------------------
        # Social Features
        # -------------------------------------------------

        student.update(
            generate_social_features(
                lifestyle_type
            )
        )

        # -------------------------------------------------
        # Privacy Features
        # -------------------------------------------------

        student.update(
            generate_privacy_features(
                lifestyle_type
            )
        )

        # -------------------------------------------------
        # Environment Features
        # -------------------------------------------------

        student.update(
            generate_environment_features(
                lifestyle_type
            )
        )

        # -------------------------------------------------
        # Personality Features
        # -------------------------------------------------

        student.update(
            generate_personality_features(
                lifestyle_type
            )
        )

        # -------------------------------------------------
        # Lifestyle Features
        # -------------------------------------------------

        student.update(
            generate_lifestyle_features(
                lifestyle_type
            )
        )

        # -------------------------------------------------
        # Financial Features
        # -------------------------------------------------

        student.update(
            generate_financial_features(
                lifestyle_type
            )
        )

        return student

    # =====================================================
    # GENERATE DATASET
    # =====================================================

    def generate_dataset( self, n_students: int = 1000):

        students = []

        for student_id in range(1, n_students + 1):

            student = self.generate_student(student_id)

            students.append(student)

        dataset = pd.DataFrame(students)

        return dataset

    # =====================================================
    # SAVE DATASET
    # =====================================================

    def save_dataset(
        self,
        dataset: pd.DataFrame,
        output_path: str
    ):

        output_path = Path(output_path)

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        dataset.to_csv(
            output_path,
            index=False
        )

        print(
            f"\nDataset saved successfully at:\n"
            f"{output_path}"
        )


# =========================================================
# MAIN EXECUTION
# =========================================================

if __name__ == "__main__":

    generator = StudentGenerator(
        seed=42
    )

    dataset = generator.generate_dataset(
        n_students=1000
    )

    print("\nDATASET PREVIEW\n")
    print(dataset.head())

    print("\nDATASET SHAPE\n")
    print(dataset.shape)

    generator.save_dataset(
        dataset,
        "data/synthetic/synthetic_students.csv"
    )

        