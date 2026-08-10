"""3033"""
def main():
    """gift wrapping"""
    size = input().split(" ")
    lenght = float(size[0])*6.28+float(size[2])
    width = float(size[1])+float(size[0])*2
    print(f"{width:.2f} {lenght:.2f}")
main()
