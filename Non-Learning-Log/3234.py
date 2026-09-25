"""3234"""
def main():
    """light"""
    light = input()
    match light[0]:
        case "R":
            start = 0
        case "G":
            start = 1
        case "B":
            start = 2
    order = ["Red","Green","Blue"]
    for i in range (int(light[2:])):
        print(order[(i+start)%3],end=" ")
main()
