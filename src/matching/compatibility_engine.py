# Feature Weights
FEATURE_WEIGHTS = {
    # Sleep & Routine
    "sleep_time": 10,
    "wake_time": 8,
    "schedule_consistency": 8,

    # Cleanliness
    "cleanliness_score": 9,

    # Study
    "study_hours": 7,

    # Personality
    "privacy_preference": 9,
    "talkativeness": 7,
    "friendship_expectation": 6,

    # Lifestyle
    "gaming_hours": 5,
    "guest_frequency": 7,

    # Environment
    "noise_sleep_tolerance": 8,
}

# Max possible difference for each feature, derived from actual data ranges.
# Used by calculate_feature_similarity() to normalise scores correctly.
FEATURE_MAX_DIFFERENCES = {
    # 1-5 scale features  ->  max diff = 4
    "schedule_consistency":   4,
    "cleanliness_score":      4,
    "privacy_preference":     4,
    "talkativeness":          4,
    "friendship_expectation": 4,
    "guest_frequency":        4,
    "noise_sleep_tolerance":  4,

    # study_hours: 1-7 scale  ->  max diff = 6
    "study_hours":  6,

    # gaming_hours: 0-8 scale  ->  max diff = 8
    "gaming_hours": 8,

    # Time features are handled separately via circular similarity
    "sleep_time": None,
    "wake_time":  None,
}

# FEATURE SIMILARITY

def calculate_feature_similarity(value_1, value_2, max_difference=5):

    # Guard: avoid ZeroDivisionError
    if max_difference == 0:
        return 1.0 if value_1 == value_2 else 0.0

    difference = abs(value_1 - value_2)

    similarity = 1 - (difference / max_difference)

    similarity = max(0, similarity)

    return similarity


def calculate_circular_similarity(value_1, value_2, max_value=24):
    """Handles circular/wrap-around comparison for 24-hour time values.
    
    E.g. 23 vs 1 → circular difference is 2, not 22.
    The maximum possible circular difference on a 24-hour clock is 12 hours.
    """
    difference = abs(value_1 - value_2)
    # Wrap-around distance (e.g. 23 vs 1 → min(22, 2) = 2)
    circular_difference = min(difference, max_value - difference)
    # Normalise: worst case circular diff on a 24-h clock is max_value / 2
    max_circular_diff = max_value / 2
    similarity = 1 - (circular_difference / max_circular_diff)
    return max(0.0, similarity)

# COMPATIBILITY SCORE

def calculate_compatibility(student_1, student_2):
    
    total_score = 0
    total_weight = 0
    feature_scores = {}

    for feature, weight in FEATURE_WEIGHTS.items():

        # Guard: skip feature if missing from either student dict
        value_1 = student_1.get(feature)
        value_2 = student_2.get(feature)
        if value_1 is None or value_2 is None:
            continue

        # Special handling for time-based features (circular 24-hour clock)
        if feature in ["sleep_time", "wake_time"]:
            similarity = calculate_circular_similarity(value_1, value_2, max_value=24)

        else:
            # Use per-feature max_difference so scores are correctly normalised
            max_diff = FEATURE_MAX_DIFFERENCES.get(feature, 4)
            similarity = calculate_feature_similarity(value_1, value_2, max_difference=max_diff)

        weighted_score = similarity * weight

        total_score += weighted_score

        total_weight += weight

        feature_scores[feature] = round(similarity * 100, 2)

    # Guard: avoid ZeroDivisionError if FEATURE_WEIGHTS is empty or all skipped
    if total_weight == 0:
        return {"compatibility_score": 0.0, "feature_scores": {}}

    compatibility_percentage = (total_score / total_weight) * 100

    return {

        "compatibility_score": round(compatibility_percentage, 2),

        "feature_scores": feature_scores
    }
