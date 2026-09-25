"""3227"""
def main():
    """card"""
    card = input()
    point = card[0:-1].upper()
    face = card[-1].upper()
    match point:
        case "J":
            point = "jack"
        case "Q":
            point = "queen"
        case "K":
            point = "king"
        case "A":
            point = "ace"
    match face:
        case "D":
            face = "diamonds"
        case "H":
            face = "hearts"
        case "S":
            face = "spades"
        case "C":
            face = "clubs"
    print(point,"of",face)
main()
