"""3357"""
def main():
    """G-raft"""
    count = 0
    giraffe = []
    unit = int(input())
    for _ in range(unit):
        giraffe.append(int(input()))
    for i in range(unit):
        if unit == 1:
            print(1)
            return
        if not i:
            if giraffe[0] > giraffe[1]:
                count += 1
        elif i == unit-1:
            if giraffe[-1] > giraffe[-2]:
                count += 1
        else:
            if giraffe[i] > giraffe[i+1] and giraffe[i] > giraffe[i-1]:
                count += 1
    print(count)
main()
