import random

from src.data.distributions import *


def generate_demographic_features():

    return generate_demographics()


# =========================================================
# SLEEP FEATURES
# =========================================================

def generate_sleep_features(lifestyle_type):

    sleep_time = generate_sleep_time(lifestyle_type)

    return {

        "sleep_time": sleep_time,

        "wake_time":
            generate_wake_time(lifestyle_type),

        "alarm_count":
            random.randint(1, 5),

        "snooze_frequency":
            random.randint(1, 5),

        "noise_sleep_tolerance":
            random.randint(1, 5),

        "lights_off_time":
            sleep_time
    }


# =========================================================
# STUDY FEATURES
# =========================================================

def generate_study_features(lifestyle_type):

    return {

        "study_hours":
            generate_study_hours(lifestyle_type),

        "study_time_preference":
            random.choice(
                [
                    "Morning",
                    "Afternoon",
                    "Evening",
                    "Night"
                ]
            ),

        "silence_requirement":
            random.randint(1, 5),

        "self_talking_study":
            random.randint(1, 5),

        "academic_seriousness":
            random.randint(1, 5)
    }


# =========================================================
# CLEANLINESS FEATURES
# =========================================================

def generate_cleanliness_features(lifestyle_type):

    cleanliness = generate_cleanliness_score(
        lifestyle_type
    )

    return {

        "cleanliness_score":
            cleanliness,

        "organization_score":
            max(
                1,
                min(
                    5,
                    cleanliness + random.randint(-1, 1)
                )
            ),

        "laundry_frequency":
            random.randint(1, 7),

        "bed_making_habit":
            random.choice([0, 1]),

        "room_cleaning_frequency":
            random.randint(1, 7),

        "bathing_frequency":
            random.randint(1, 3),

        "towel_management":
            random.randint(1, 5)
    }


# =========================================================
# SOCIAL FEATURES
# =========================================================

def generate_social_features(lifestyle_type):

    return {

        "phone_call_frequency":
            random.randint(1, 5),

        "late_night_calls":
            random.randint(1, 5),

        "talkativeness":
            generate_talkativeness(lifestyle_type),

        "guest_frequency":
            generate_guest_frequency(lifestyle_type),

        "overnight_guest_comfort":
            generate_overnight_guest_comfort(
                lifestyle_type
            ),

        "friendship_expectation":
            generate_friendship_expectation(
                lifestyle_type
            ),

        "guest_timing_preference":
            random.choice(
                [
                    "Morning",
                    "Afternoon",
                    "Evening",
                    "Anytime"
                ]
            )
    }


# =========================================================
# PRIVACY FEATURES
# =========================================================

def generate_privacy_features(lifestyle_type):

    return {

        "privacy_preference":
            generate_privacy_preference(
                lifestyle_type
            ),

        "sharing_comfort":
            generate_sharing_comfort(
                lifestyle_type
            ),

        "boundary_importance":
            generate_boundary_importance(
                lifestyle_type
            ),

        "unauthorized_usage":
            generate_unauthorized_usage(
                lifestyle_type
            ),

        "borrowing_frequency":
            random.randint(1, 5),

        "independence_preference":
            generate_independence_preference(
                lifestyle_type
            )
    }


# =========================================================
# ENVIRONMENT FEATURES
# =========================================================

def generate_environment_features(lifestyle_type):

    return {

        "fan_speed_preference":
            generate_fan_speed_preference(),

        "temperature_preference":
            generate_temperature_preference(),

        "entry_exit_noise_awareness":
            generate_entry_exit_noise_awareness(
                lifestyle_type
            )
    }


# =========================================================
# PERSONALITY FEATURES
# =========================================================

def generate_personality_features(lifestyle_type):

    return {

        "conflict_tolerance":
            generate_conflict_tolerance(
                lifestyle_type
            ),

        "conflict_style":
            generate_conflict_style(
                lifestyle_type
            ),

        "criticism_response":
            generate_criticism_response(
                lifestyle_type
            ),

        "emotional_stability":
            generate_emotional_stability(
                lifestyle_type
            ),

        "negativity_level":
            generate_negativity_level(
                lifestyle_type
            ),

        "communication_respect":
            generate_communication_respect(
                lifestyle_type
            ),

        "punctuality":
            random.randint(1, 5),

        "adaptability":
            generate_adaptability(
                lifestyle_type
            ),

        "schedule_consistency":
            generate_schedule_consistency(
                lifestyle_type
            )
    }


# =========================================================
# LIFESTYLE HABITS
# =========================================================

def generate_lifestyle_features(lifestyle_type):

    return {

        "smoking":
            generate_smoking(lifestyle_type),

        "drinking":
            generate_drinking(lifestyle_type),

        "gaming_hours":
            generate_gaming_hours(lifestyle_type),

        "music_frequency":
            generate_music_frequency(
                lifestyle_type
            ),

        "music_volume":
            generate_music_volume(
                lifestyle_type
            ),

        "room_eating_habit":
            generate_room_eating_habit(),

        "food_smell_tolerance":
            generate_food_smell_tolerance(
                lifestyle_type
            ),

        "food_preference":
            generate_food_preference(),

        "gym_frequency":
            generate_gym_frequency(
                lifestyle_type
            ),

        "religious_practice_frequency":
            generate_religious_practice_frequency()
    }


# =========================================================
# FINANCIAL FEATURES
# =========================================================

def generate_financial_features(lifestyle_type):

    return {

        "expense_responsibility":
            generate_expense_responsibility(
                lifestyle_type
            )
    }