"""3022"""
def main():
    """temperature"""
    temp = float(input())
    unit1 = input()
    unit2 = input()
    match unit1:
        case "C":
            pass
        case "K":
            temp -= 273.15
        case "F":
            temp = (temp-32)*5/9
        case "R":
            temp = (temp-491.67)*5/9
    match unit2:
        case "C":
            pass
        case "K":
            temp += 273.15
        case "F":
            temp = temp*1.8+32
        case "R":
            temp = temp*9/5+491.67
    print(f"{temp:.2f}")
main()
