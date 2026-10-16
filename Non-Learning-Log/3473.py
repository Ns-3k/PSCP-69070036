"""3473"""
def main():
    """arrow"""
    s = input()
    for i in range(5):
        line = ""
        for c in s:
            if c == "U":
                arrow = ["  *  ", " *** ", "* * *", "  *  ", "  *  "]
            elif c == "D":
                arrow = ["  *  ", "  *  ", "* * *", " *** ", "  *  "]
            elif c == "L":
                arrow = ["  *  ", " *   ", "*****", " *   ", "  *  "]
            else:
                arrow = ["  *  ", "   * ", "*****", "   * ", "  *  "]
            line += arrow[i] + " "
        print(line)
main()
