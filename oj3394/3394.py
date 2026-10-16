"""3394"""
def main():
    """0_o"""
    n, s = map(int, input().split())
    students = []
    for _ in range(n):
        students.append(int(input()))
    passed = set()
    current = s
    while current and current not in passed:
        passed.add(current)
        current = students[current - 1]
    print(len(passed))
main()
