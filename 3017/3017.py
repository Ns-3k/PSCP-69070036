"""3017"""
def main():
    """bill"""
    food = int(input())
    if food/10 <= 50 :
        service = 50
    elif food/10 <= 1000 :
        service = food/10
    else :
        service = 1000
    print(f"{(food + service) + (food + service)*0.07:.2f}")
main()
