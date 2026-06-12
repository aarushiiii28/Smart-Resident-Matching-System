import random


def generate_lifestyle_type():
    """ 
    Generate a studdent lifestyle profile

    Returns:
       str
    """

    lifestyles = [
        "disciplined",
        "average",
        "night_owl",
        "social",
        "introvert",
        "clean_freak",
        "gamer",
        "fitness_focused"
    ]

    
    weights = [
        0.15,
        0.30,
        0.10,
        0.10,
        0.10,
        0.08,
        0.10,
        0.07
    ]

    return random.choices(
        lifestyles,
        weights=weights,
        k=1
    )[0]

def generate_sleep_time(lifestyle_type):
    """ 
    Generate realistic sleep time.
    Stored in 24-hour format.
    """
    if lifestyle_type == "disciplined":
        return random.randint(21,23)

    if lifestyle_type == "night_owl":
        return random.randint(1, 4)

    if lifestyle_type == "social":
        return random.choice([23, 0, 1])

    if lifestyle_type == "introvert":
        return random.randint(22, 24)

    return random.choice([22, 23, 0, 1])

def generate_wake_time(lifestyle_type):

    if lifestyle_type == "disciplined":
        return random.randint(5, 7)

    if lifestyle_type == "night_owl":
        return random.randint(8, 11)

    if lifestyle_type == "social":
        return random.randint(7, 9)

    if lifestyle_type == "introvert":
        return random.randint(6, 8)

    return random.randint(6, 9)

def generate_cleanliness_score(lifestyle_type):

    if lifestyle_type == "disciplined":
        return random.randint(4, 5)

    if lifestyle_type == "introvert":
        return random.randint(3, 5)

    if lifestyle_type == "night_owl":
        return random.randint(2, 4)

    return random.randint(2, 4)

def generate_study_hours(lifestyle_type):

    if lifestyle_type == "disciplined":
        return random.randint(3, 7)

    if lifestyle_type == "night_owl":
        return random.randint(2, 6)

    if lifestyle_type == "social":
        return random.randint(1, 4)

    return random.randint(2, 5)

def generate_guest_frequency(lifestyle_type):

    if lifestyle_type == "social":
        return random.randint(4, 5)

    if lifestyle_type == "introvert":
        return 1

    if lifestyle_type == "disciplined":
        return random.randint(1, 2)

    return random.randint(2, 3)

def generate_privacy_preference(lifestyle_type):

    if lifestyle_type in ["introvert", "clean_freak"]:
        return random.randint(4, 5)

    if lifestyle_type == "social":
        return random.randint(1, 3)

    return random.randint(2, 4)


def generate_sharing_comfort(lifestyle_type):

    if lifestyle_type == "social":
        return random.randint(4, 5)

    if lifestyle_type == "introvert":
        return random.randint(1, 3)

    return random.randint(2, 4)


def generate_boundary_importance(lifestyle_type):

    if lifestyle_type in ["introvert", "clean_freak"]:
        return random.randint(4, 5)

    return random.randint(2, 4)


def generate_independence_preference(lifestyle_type):

    if lifestyle_type == "introvert":
        return random.randint(4, 5)

    if lifestyle_type == "social":
        return random.randint(1, 3)

    return random.randint(2, 4)

def generate_talkativeness(lifestyle_type):

    if lifestyle_type == "social":
        return random.randint(4, 5)

    if lifestyle_type == "introvert":
        return random.randint(1, 2)

    return random.randint(2, 4)


def generate_friendship_expectation(lifestyle_type):

    if lifestyle_type == "social":
        return random.randint(4, 5)

    if lifestyle_type == "introvert":
        return random.randint(1, 2)

    return random.randint(2, 4)


def generate_adaptability(lifestyle_type):

    if lifestyle_type in ["fitness_focused", "disciplined"]:
        return random.randint(4, 5)

    return random.randint(2, 4)


def generate_schedule_consistency(lifestyle_type):

    if lifestyle_type in [
        "disciplined",
        "fitness_focused"
    ]:
        return random.randint(4, 5)

    if lifestyle_type in [
        "night_owl",
        "gamer"
    ]:
        return random.randint(1, 3)

    return random.randint(2, 4)


def generate_conflict_tolerance(lifestyle_type):

    if lifestyle_type == "social":
        return random.randint(3, 5)

    return random.randint(2, 4)

def generate_gaming_hours(lifestyle_type):

    if lifestyle_type == "gamer":
        return random.randint(4, 8)

    if lifestyle_type == "disciplined":
        return random.randint(0, 2)

    return random.randint(1, 4)


def generate_gym_frequency(lifestyle_type):

    if lifestyle_type == "fitness_focused":
        return random.randint(5, 7)

    return random.randint(0, 4)


def generate_smoking(lifestyle_type):

    if lifestyle_type == "fitness_focused":
        return 0

    return random.choice([0, 0, 0, 1])


def generate_drinking(lifestyle_type):

    if lifestyle_type == "fitness_focused":
        return 0

    return random.choice([0, 0, 1])

def generate_fan_speed_preference():

    return random.randint(1, 5)


def generate_temperature_preference():

    return random.randint(1, 5)


def generate_entry_exit_noise_awareness(lifestyle_type):

    if lifestyle_type in [
        "disciplined",
        "clean_freak"
    ]:
        return random.randint(4, 5)

    return random.randint(2, 4)

def generate_expense_responsibility(lifestyle_type):

    if lifestyle_type in [
        "disciplined",
        "fitness_focused"
    ]:
        return random.randint(4, 5)

    return random.randint(2, 4)

def generate_emotional_stability(lifestyle_type):

    if lifestyle_type in [
        "disciplined",
        "fitness_focused"
    ]:
        return random.randint(4, 5)

    if lifestyle_type == "gamer":
        return random.randint(2, 4)

    return random.randint(2, 5)


def generate_negativity_level(lifestyle_type):

    if lifestyle_type in [
        "social",
        "fitness_focused"
    ]:
        return random.randint(1, 3)

    return random.randint(1, 5)


def generate_communication_respect(lifestyle_type):

    if lifestyle_type in [
        "disciplined",
        "fitness_focused",
        "clean_freak"
    ]:
        return random.randint(4, 5)

    return random.randint(2, 5)


def generate_criticism_response(lifestyle_type):

    if lifestyle_type == "social":
        return random.randint(3, 5)

    return random.randint(2, 5)


def generate_conflict_style(lifestyle_type):

    styles = [
        "Direct",
        "Avoid",
        "Complain",
        "Aggressive"
    ]

    if lifestyle_type == "introvert":
        return random.choice(
            ["Avoid", "Avoid", "Direct"]
        )

    if lifestyle_type == "social":
        return random.choice(
            ["Direct", "Direct", "Complain"]
        )

    return random.choice(styles)

def generate_music_frequency(lifestyle_type):

    if lifestyle_type in [
        "social",
        "gamer"
    ]:
        return random.randint(4, 5)

    return random.randint(1, 4)


def generate_music_volume(lifestyle_type):

    if lifestyle_type == "social":
        return random.randint(3, 5)

    if lifestyle_type == "introvert":
        return random.randint(1, 3)

    return random.randint(1, 5)


def generate_room_eating_habit():

    return random.choice([0, 1])


def generate_food_smell_tolerance(lifestyle_type):

    if lifestyle_type == "clean_freak":
        return random.randint(1, 3)

    return random.randint(2, 5)


def generate_food_preference():

    return random.choice(
        [
            "Vegetarian",
            "Non-Vegetarian",
            "Eggetarian"
        ]
    )


def generate_religious_practice_frequency():

    return random.randint(1, 5)

def generate_unauthorized_usage(lifestyle_type):

    if lifestyle_type in [
        "disciplined",
        "clean_freak"
    ]:
        return 0

    return random.choice([0, 0, 0, 1])

def generate_overnight_guest_comfort(lifestyle_type):

    if lifestyle_type == "social":
        return 1

    if lifestyle_type == "introvert":
        return 0

    return random.choice([0, 1])

# Demographics
def generate_demographics():

    return {

        "age": random.randint(18, 24),

        "gender": random.choice(
            [
                "Male",
                "Female"
            ]
        ),

        "course": random.choice(
            [
                "CSE",
                "ECE",
                "ME",
                "CE",
                "EE",
                "IT",
                "BBA",
                "BCOM"
            ]
        ),

        "year_of_study": random.randint(1, 4),

        "hostel_block": random.choice(
            [
                "A",
                "B",
                "C",
                "D"
            ]
        )
    }