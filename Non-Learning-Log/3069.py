"""3069"""
def main():
    """zodiac"""
    day = int(input())
    month = int(input())
    date = day+((month-1)*30)
    if date <= 19 or date > 351:
        print("capricorn")
    elif date <= 48:
        print("aquarius")
    elif date <= 80:
        print("pisces")
    elif date <= 109:
        print("aries")
    elif date <= 140:
        print("taurus")
    elif date <= 171:
        print("gemini")
    elif date <= 202:
        print("cancer")
    elif date <= 232:
        print("leo")
    elif date <= 262:
        print("virgo")
    elif date <= 293:
        print("libra")
    elif date <= 321:
        print("scorpio")
    else:
        print("sagittarius")
main()
