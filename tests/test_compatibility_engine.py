import pandas as pd

from src.matching.compatibility_engine import (
    calculate_compatibility
)

from src.data.student_generator import (
    StudentGenerator
)


generator = StudentGenerator()

dataset = generator.generate_dataset(
    n_students=5
)

student_1 = dataset.iloc[0]

student_2 = dataset.iloc[1]

result = calculate_compatibility(
    student_1,
    student_2
)

print("\nSTUDENT 1")
print(student_1["lifestyle_type"])

print("\nSTUDENT 2")
print(student_2["lifestyle_type"])

print("\nCOMPATIBILITY RESULT")
print(result)