"""3474"""
def main():
    """qwerty"""
    res = {
        "black": 0, "brown": 1, "red": 2, "orange": 3,
        "yellow": 4, "green": 5, "blue": 6, "purple": 7,
        "grey": 8, "white": 9
    }
    mult = {
        "black": 1, "brown": 10, "red": 100, "orange": 1000,
        "yellow": 10000, "green": 100000, "blue": 1000000,
        "purple": 10000000, "gold": 0.1, "silver": 0.01
    }
    tol = {
        "brown": 0.01, "red": 0.02, "green": 0.005,
        "blue": 0.0025, "purple": 0.001, "grey": 0.0005,
        "gold": 0.05, "silver": 0.10
    }
    c1 = input().lower()
    c2 = input().lower()
    c3 = input().lower()
    c4 = input().lower()
    if c1 not in res or c2 not in res or c3 not in mult or c4 not in tol:
        print("Error")
        return
    value = (res[c1] * 10 + res[c2]) * mult[c3]
    tolerance = tol[c4]
    print(f"{value * (1 - tolerance):.4f}")
    print(f"{value * (1 + tolerance):.4f}")
main()
