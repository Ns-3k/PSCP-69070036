"""3032"""
def main():
    """test"""
    rabbit = int(input())
    topscore = 0
    top = 0
    for _ in range(0,rabbit):
        score = int(input())
        if score > topscore:
            topscore = score
            top = 1
        elif score == topscore:
            top += 1
        else:
            pass
    print(topscore)
    print(top)
main()
