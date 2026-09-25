"""3293"""
def main():
    """frame"""
    line1 = input()
    line2 = input()
    line3 = input()
    line4 = input()
    line5 = input()
    frame = max(len(line1),len(line2),len(line3),len(line4),len(line5))
    print(frame)
    print("*"*frame)
main()