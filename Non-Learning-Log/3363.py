"""3363"""
def main():
    """cvx"""
    r,c = map(int,input().split())
    target = list(map(int,input().split()))
    chance = 0
    count = r*c
    infected = []
    n = int(input())
    for _ in range(n):
        infected.append(list(map(int,input().split())))
    for i in range(r):
        for j in range(c):
            if any(not abs(i - p[0]) and not abs(j - p[1]) for p in infected):
                count -= 1
                if [i,j] == target:
                    chance = 100
            elif any(abs(i - p[0]) <= 1 and abs(j - p[1]) <= 1 for p in infected):
                count -= 1
                if [i,j] == target:
                    chance = 60
            elif any(abs(i - p[0]) <= 2 and abs(j - p[1]) <= 2 for p in infected):
                count -= 1
                if [i,j] == target:
                    chance = 20
    print(f"{count}\n{chance}%")
main()
