"""3165"""
def main():
    """walk"""
    move = input()
    x,y = 0,0
    for ch in move:
        match ch:
            case "N":
                y += 1
            case "E":
                x += 1
            case "W":
                x -= 1
            case "S":
                y -= 1
    print(x,y,abs(x)+abs(y))
main()
