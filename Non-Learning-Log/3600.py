"""3600"""
def main():
    """cal"""
    cal = 0
    order = "adadadad"
    while order != "5":
        order = input()
        match order:
            case "1":
                cal += 100
            case "2":
                cal += 120
            case "3":
                cal += 200
            case "4":
                cal += 60
    print(f"Bye Bye\nTotal Calories: {cal}")
main()
