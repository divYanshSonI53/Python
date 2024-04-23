# Friday, 12th April

# 10. Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

pet_species = input("Provide pet species: ").strip().lower()
pet_age = int(input("Provide pet age: "))

if pet_species == "dog":
    if pet_age < 2:
        print("Puppy food")
    else:
        print("Senior Cat food")

if pet_species == "cat":
    if pet_age > 5:
        print("Senior cat food")
    else:
        print("Junior cat food")