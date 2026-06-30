import pandas as pd

# ============================================================================
# REQUIRED MODEL FEATURES
# ============================================================================

MODEL_FIELDS = [
    "sleep_time",
    "wake_time",
    "gaming_hours",
    "cleanliness_score",
    "privacy_preference",
    "noise_sleep_tolerance",
    "lifestyle_type"
]

# ============================================================================
# VALIDATION
# ============================================================================

def _validate_student(student: dict, label: str = "student") -> None:

    missing = [
        field
        for field in MODEL_FIELDS
        if field not in student
    ]

    if missing:
        raise KeyError(
            f"{label} is missing required fields: {missing}"
        )

# ============================================================================
# SIMILARITY FUNCTIONS
# ============================================================================

def calculate_similarity(
    value_1,
    value_2,
    max_difference
) -> float:

    if max_difference == 0:
        return 1.0

    difference = abs(value_1 - value_2)

    similarity = 1 - (
        difference / max_difference
    )

    return max(0.0, similarity)


def calculate_time_similarity(
    time_1,
    time_2
) -> float:

    difference = abs(time_1 - time_2)

    circular_difference = min(
        difference,
        24 - difference
    )

    similarity = 1 - (
        circular_difference / 12
    )

    return max(0.0, similarity)

# ============================================================================
# MAIN FEATURE ENGINEERING
# ============================================================================

def create_pairwise_features(
    student_1: dict,
    student_2: dict
) -> pd.DataFrame:

    _validate_student(
        student_1,
        "student_1"
    )

    _validate_student(
        student_2,
        "student_2"
    )

    features = {}

    # ========================================================================
    # RAW FEATURES
    # ========================================================================

    for field in MODEL_FIELDS:

        features[f"{field}_1"] = student_1[field]

        features[f"{field}_2"] = student_2[field]

    # ========================================================================
    # SLEEP FEATURES
    # ========================================================================

    sleep_diff = abs(
        student_1["sleep_time"]
        -
        student_2["sleep_time"]
    )

    sleep_diff = min(
        sleep_diff,
        24 - sleep_diff
    )

    features["sleep_time_diff"] = sleep_diff

    features["sleep_time_similarity"] = (
        calculate_time_similarity(
            student_1["sleep_time"],
            student_2["sleep_time"]
        )
    )

    # ========================================================================
    # WAKE FEATURES
    # ========================================================================

    wake_diff = abs(
        student_1["wake_time"]
        -
        student_2["wake_time"]
    )

    wake_diff = min(
        wake_diff,
        24 - wake_diff
    )

    features["wake_time_diff"] = wake_diff

    features["wake_time_similarity"] = (
        calculate_time_similarity(
            student_1["wake_time"],
            student_2["wake_time"]
        )
    )

    # ========================================================================
    # GAMING FEATURES
    # ========================================================================

    features["gaming_hours_diff"] = abs(
        student_1["gaming_hours"]
        -
        student_2["gaming_hours"]
    )

    features["gaming_hours_similarity"] = (
        calculate_similarity(
            student_1["gaming_hours"],
            student_2["gaming_hours"],
            max_difference=8
        )
    )

    # ========================================================================
    # CLEANLINESS FEATURES
    # ========================================================================

    features["cleanliness_score_diff"] = abs(
        student_1["cleanliness_score"]
        -
        student_2["cleanliness_score"]
    )

    features["cleanliness_score_similarity"] = (
        calculate_similarity(
            student_1["cleanliness_score"],
            student_2["cleanliness_score"],
            max_difference=4
        )
    )

    # ========================================================================
    # PRIVACY FEATURES
    # ========================================================================

    features["privacy_preference_diff"] = abs(
        student_1["privacy_preference"]
        -
        student_2["privacy_preference"]
    )

    features["privacy_compatibility"] = (
        calculate_similarity(
            student_1["privacy_preference"],
            student_2["privacy_preference"],
            max_difference=4
        )
    )

    # ========================================================================
    # NOISE FEATURES
    # ========================================================================

    features["noise_sleep_tolerance_diff"] = abs(
        student_1["noise_sleep_tolerance"]
        -
        student_2["noise_sleep_tolerance"]
    )

    features["noise_sleep_tolerance_similarity"] = (
        calculate_similarity(
            student_1["noise_sleep_tolerance"],
            student_2["noise_sleep_tolerance"],
            max_difference=4
        )
    )

    # ========================================================================
    # CATEGORY COMPATIBILITY FEATURES
    # ========================================================================

    features["sleep_compatibility"] = (
        features["sleep_time_similarity"]
        +
        features["wake_time_similarity"]
    ) / 2

    features["cleanliness_compatibility"] = (
        features["cleanliness_score_similarity"]
    )

    features["social_compatibility"] = (
        features["gaming_hours_similarity"]
    )

    # ========================================================================
    # LIFESTYLE
    # ========================================================================

    features["same_lifestyle_type"] = int(
        student_1["lifestyle_type"]
        ==
        student_2["lifestyle_type"]
    )

    # ========================================================================
    # BEHAVIORAL ALIGNMENT
    # ========================================================================

    similarity_signals = [

        features["sleep_time_similarity"],

        features["wake_time_similarity"],

        features["gaming_hours_similarity"],

        features["cleanliness_score_similarity"],

        features["privacy_compatibility"],

        features["noise_sleep_tolerance_similarity"]
    ]

    features["behavioral_alignment_score"] = (

        sum(similarity_signals) / len(similarity_signals)
    )

    return pd.DataFrame([features])