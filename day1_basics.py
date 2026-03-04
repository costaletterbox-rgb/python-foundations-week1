# Day 1 - Basics: lists + loops

foods = ["Pizza", "Sushi", "Pasta", "Burger", "Salad"]

print("My favourite foods:")
for food in foods:
    print("-", food)
    # Day 1 - Basics: dictionaries

ages = {"Kosta": 42, "Maria": 35, "John": 28}

print("\nAges:")
for name, age in ages.items():
    print(f"{name} is {age} years old")