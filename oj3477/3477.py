"""3477"""
def main():
    """Pad Thai"""
    ings = [
        "Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp",
        "Bean Sprouts", "Noodle", "Chives", "Lime",
        "Egg", "Oil", "Peanuts"
    ]
    tastes = ["Sweet", "Sour", "Salty"]
    used_ings = []
    used_tastes = []
    bad_ing = False
    while True:
        ing = input()
        if ing == "Cook":
            break
        if ing not in ings:
            bad_ing = True
        used_ings.append(ing)
    while True:
        taste = input()
        if taste == "End":
            break
        used_tastes.append(taste)
    if bad_ing:
        print("This is not Pad Thai!!!")
    elif any(ing not in used_ings for ing in ings):
        print("This is bad!")
    elif any(taste not in tastes for taste in used_tastes) or \
    any(taste not in used_tastes for taste in tastes):
        print("Not Bad...")
    else:
        print("Delicious!")
main()
