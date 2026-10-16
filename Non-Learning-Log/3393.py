"""3393"""
def main():
    """cave n no cliff"""
    n = int(input())
    cave = list(map(int, input().split()))
    s = input()
    pos = cave.index(1)
    treasure = cave.index(2)
    for move in s:
        if move == "R":
            next_pos = pos + 1
        else:
            next_pos = pos - 1
        if next_pos < 0 or next_pos >= n:
            continue
        pos = next_pos
        if pos == treasure:
            break
    cave[cave.index(1)] = 0
    cave[pos] = 1
    print(*cave)
main()
