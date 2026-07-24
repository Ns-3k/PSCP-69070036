"""3063"""
def main():
    """safe"""
    char = input()
    num = input()
    password = "H4567"
    password_in = char + num
    if password_in == password :
        print("safe unlocked")
    elif password_in[0] == "H":
        print("safe locked - change digit")
    elif password_in[-1:-5:-1] == "7654":
        print("safe locked - change char")
    else :
        print("safe locked")
main()
