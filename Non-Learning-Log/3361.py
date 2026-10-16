"""3361"""
def main():
    """car go vroom"""
    n = int(input())
    cars = []
    count = 0
    car_v = 0
    car = []
    for _ in range (n):
        car = list(map(int,input().split()))
        cars.append(car)
    for i in range(n-1,-1,-1):
        if cars[i][1] < car_v :
            count += 1
        else:
            car_v = cars[i][1]
    print(count)
main()
