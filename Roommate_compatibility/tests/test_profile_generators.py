from src.data.distributions import generate_lifestyle_type
from src.data.profile_generators import *

lifestyle = generate_lifestyle_type()

print("\nLIFESTYLE")
print(lifestyle)

print("\nDEMOGRAPHICS")
print(generate_demographic_features())

print("\nSLEEP")
print(generate_sleep_features(lifestyle))

print("\nSTUDY")
print(generate_study_features(lifestyle))

print("\nCLEANLINESS")
print(generate_cleanliness_features(lifestyle))

print("\nSOCIAL")
print(generate_social_features(lifestyle))

print("\nPRIVACY")
print(generate_privacy_features(lifestyle))

print("\nENVIRONMENT")
print(generate_environment_features(lifestyle))

print("\nPERSONALITY")
print(generate_personality_features(lifestyle))

print("\nLIFESTYLE HABITS")
print(generate_lifestyle_features(lifestyle))

print("\nFINANCIAL")
print(generate_financial_features(lifestyle))