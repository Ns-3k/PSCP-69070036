"""3484"""
def main():
    """wqeiq"""
    n, p = input().split()
    n = int(n)
    p = float(p)
    tiles = []
    row_tiles = []
    row_points = []
    col_tiles = [0] * n
    col_points = [0] * n
    total_tiles = 0
    total_points = 0
    for i in range(n):
        row = list(map(int, input().split()))
        tiles.append(row)
        bad_tiles = 0
        bad_points = 0
        for j in range(n):
            if row[j] > 0:
                bad_tiles += 1
                total_tiles += 1
                col_tiles[j] += 1
            bad_points += row[j]
            total_points += row[j]
            col_points[j] += row[j]
        row_tiles.append(bad_tiles)
        row_points.append(bad_points)
    for i in range(n):
        print(*tiles[i], row_tiles[i], row_points[i])
    print(*col_tiles)
    print(*col_points)
    print(total_tiles, total_points, f"{total_points * p:.2f}")
main()
