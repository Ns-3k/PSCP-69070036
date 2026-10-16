"""3479"""
def main():
    """qwe"""
    card = input().upper()
    values = {
        "A": "Ace","J": "Jack","Q": "Queen","K": "King"
    }
    faces = {
        "D": "Diamonds","H": "Hearts","S": "Spades","C": "Clubs"
    }
    value = card[:-1]
    face = card[-1]
    print(values.get(value, value), "of", faces[face])
main()
