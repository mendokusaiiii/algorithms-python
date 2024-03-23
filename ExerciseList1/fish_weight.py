def calculate_fish(fish_weight):
    fish_limit = 50
    fine_per_kg = 4.00

    if fish_weight > fish_limit:
        excess = fish_weight - fish_limit
        fine = excess * fine_per_kg
    else:
        excess = 0
        fine = 0

    return excess, fine

fish_weight = float(input("Digit the weight of the fish: "))

excess, fine = calculate_fish(fish_weight)

if excess > 0:
    print("Excess weight: ", excess)
    print(f"Fine: ", fine)
else:
    print("There was no excess weight")
