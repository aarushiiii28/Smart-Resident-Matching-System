# -*- coding: utf-8 -*-
import random
from pathlib import Path

import numpy as np
import pandas as pd

from src.data.student_generator import StudentGenerator
from src.matching.compatibility_engine import calculate_compatibility


class PairwiseDatasetGenerator:

    def __init__(self, seed: int = 42):

        random.seed(seed)
        np.random.seed(seed)          # keep numpy RNG in sync with random

        self.generator = StudentGenerator(seed=seed)

    # =========================================================
    # GENERATE PAIRWISE DATASET
    # =========================================================

    def generate_pairwise_dataset(
        self,
        n_students: int = 500,
        n_pairs: int = 10_000,
        verbose: bool = True
    ) -> pd.DataFrame:
        """
        Generate a dataset of n_pairs student pairs with their
        compatibility scores.

        Optimisations over the naive approach:
        - Pre-converts the student DataFrame to a list of dicts once,
          avoiding repeated .iloc[] calls (O(1) dict lookup vs O(n) iloc).
        - Builds the pair index pool once and samples from it each iteration.
        - Uses a single dict merge per pair instead of two column loops.
        - Collects rows as a list of dicts and constructs the DataFrame once
          at the end (avoids repeated DataFrame appends).
        """

        if verbose:
            print(f"Generating {n_students} students...")

        students_df = self.generator.generate_dataset(n_students=n_students)

        # Pre-convert to list of dicts for O(1) access per pair
        students = students_df.to_dict(orient="records")
        n = len(students)
        index_pool = list(range(n))

        if verbose:
            print(f"Building {n_pairs:,} pairwise combinations...")

        pairwise_rows = []

        for i in range(n_pairs):

            idx_1, idx_2 = random.sample(index_pool, 2)

            student_1 = students[idx_1]
            student_2 = students[idx_2]

            compatibility_result = calculate_compatibility(student_1, student_2)

            # Merge both student dicts with suffixes + target in one step
            row = (
                {f"{col}_1": val for col, val in student_1.items()}
                | {f"{col}_2": val for col, val in student_2.items()}
                | {"compatibility_score": compatibility_result["compatibility_score"]}
            )

            pairwise_rows.append(row)

            if verbose and (i + 1) % 2000 == 0:
                print(f"  {i + 1:,} / {n_pairs:,} pairs done")

        pairwise_df = pd.DataFrame(pairwise_rows)

        if verbose:
            print(f"Done. Dataset shape: {pairwise_df.shape}")

        return pairwise_df

    # =========================================================
    # SAVE DATASET
    # =========================================================

    def save_dataset(
        self,
        dataset: pd.DataFrame,
        output_path: str
    ) -> None:
        """Save the dataset to a CSV file, creating parent dirs if needed."""

        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        dataset.to_csv(path, index=False)

        print(f"\nDataset saved at:\n{path}")


# =========================================================
# MAIN
# =========================================================

if __name__ == "__main__":

    generator = PairwiseDatasetGenerator(seed=42)

    pairwise_df = generator.generate_pairwise_dataset(
        n_students=500,
        n_pairs=10_000,
        verbose=True
    )

    print("\nPAIRWISE DATASET PREVIEW\n")
    print(pairwise_df.head())

    print("\nDATASET SHAPE\n")
    print(pairwise_df.shape)

    generator.save_dataset(
        pairwise_df,
        "data/pairwise/pairwise_compatibility.csv"
    )