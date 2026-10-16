"""3390"""
def main():
    """odd"""
    array = [list(map(int, input().split())) for _ in range(5)]
    odd_rows = []
    odd_cols = []
    for row in range(5):
        if sum(array[row]) % 2:
            odd_rows.append(row)
    for col in range(5):
        total = sum(array[row][col] for row in range(5))
        if total % 2:
            odd_cols.append(col)
    if len(odd_rows) == 1 and len(odd_cols) == 1:
        print(odd_rows[0], odd_cols[0])
    else:
        print(-1, -1)
main()
