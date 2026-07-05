"""3011"""
def red(color):
    """red"""
    if color == "Red" :
        print ("Red")
    elif color == "Blue" :
        print ("Violet")
    elif color == "Yellow" :
        print ("Orange")
    else :
        print("Error")
def yellow(color):
    """yellow"""
    if color == "Red" :
        print ("Orange")
    elif color == "Blue" :
        print ("Green")
    elif color == "Yellow" :
        print ("Yellow")
    else :
        print("Error")
def blue(color):
    """blue"""
    if color == "Red" :
        print ("Violet")
    elif color == "Blue" :
        print ("Blue")
    elif color == "Yellow" :
        print ("Green")
    else :
        print("Error")
def main():
    """color mix"""
    color1 = input()
    color2 = input()
    match color1 :
        case "Red" :
            red(color2)
        case "Yellow" :
            yellow(color2)
        case "Blue" :
            blue(color2)
        case _:
            print ("Error")
main()
