"""3300"""
def main():
    """fahhhh"""
    n = int(input())
    overwork = False
    big_work = []
    small_work = []
    count = 0
    for _ in range(n):
        temp = int(input())
        if temp > 18:
            big_work.append(temp)
        else:
            small_work.append(temp)
    while big_work or small_work:
        if big_work and not overwork:
            big_work.pop()
            overwork = True
            count += 1
        if small_work:
            small_work.pop()
            overwork = False
            count += 1
        elif big_work or small_work:
            overwork = False
            count += 1
    print(count)
main()
