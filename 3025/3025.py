"""3025"""
def main():
    """season"""
    month = int(input())
    day = int(input())
    if day >= 21 and not month%3:
        month += 1
        if month == 13:
            month = 1
    if month <= 3:
        season = "winter"
    elif month <= 6:
        season = "spring"
    elif month <= 9:
        season = "summer"
    else:
        season = "fall"
    print(season)
main()
