from src.data.distributions import *


for _ in range(5):

    lifestyle = generate_lifestyle_type()

    print("\n==============================")
    print(f"LIFESTYLE TYPE: {lifestyle}")
    print("==============================")

    print("\nDEMOGRAPHICS")
    print(generate_demographics())

    print("\nSLEEP FEATURES")
    print({
        "sleep_time": generate_sleep_time(lifestyle),
        "wake_time": generate_wake_time(lifestyle)
    })

    print("\nPRIVACY FEATURES")
    print({
        "privacy_preference":
            generate_privacy_preference(lifestyle),

        "sharing_comfort":
            generate_sharing_comfort(lifestyle),

        "boundary_importance":
            generate_boundary_importance(lifestyle),

        "independence_preference":
            generate_independence_preference(lifestyle)
    })

    print("\nPERSONALITY FEATURES")
    print({
        "talkativeness":
            generate_talkativeness(lifestyle),

        "friendship_expectation":
            generate_friendship_expectation(lifestyle),

        "adaptability":
            generate_adaptability(lifestyle),

        "schedule_consistency":
            generate_schedule_consistency(lifestyle),

        "conflict_tolerance":
            generate_conflict_tolerance(lifestyle)
    })

    print("\nLIFESTYLE FEATURES")
    print({
        "gaming_hours":
            generate_gaming_hours(lifestyle),

        "gym_frequency":
            generate_gym_frequency(lifestyle),

        "smoking":
            generate_smoking(lifestyle),

        "drinking":
            generate_drinking(lifestyle)
    })

    print("\nENVIRONMENT FEATURES")
    print({
        "fan_speed_preference":
            generate_fan_speed_preference(),

        "temperature_preference":
            generate_temperature_preference(),

        "entry_exit_noise_awareness":
            generate_entry_exit_noise_awareness(lifestyle)
    })

    print("\nFINANCIAL FEATURES")
    print({
        "expense_responsibility":
            generate_expense_responsibility(lifestyle)
    })