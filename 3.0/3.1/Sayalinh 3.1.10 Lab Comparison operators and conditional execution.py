plant = input("Get me a plant: ")

if plant == "Spathiphyllum": print("Yes - Spathiphyllum is the best plant ever!")
elif plant == "spathiphyllum": print("No, I want a big Spathiphyllum!")
#else: print("Spathiphyllum! Not", plant + "!")

# Using the max() for booleans like or operators

if not (max(plant == "spathiphyllum", plant == "Spathiphyllum")): print("Spathiphyllum! Not", plant + "!")

# This can be done with min() to work like an and operator, however, within the
# given bounds of the assignment I can't implement this without different input
