"""3483"""
def main():
    """sdasd"""
    n, m = map(int, input().split())
    if not 1 <= n <= 10 or not 1 <= m <= 20:
        print("Data Incorrect")
        return

    scores = []
    total = 0
    for i in range(n):
        team = list(map(int, input().split()))
        if len(team) != m or any(score < 0 or score > 100 for score in team):
            print("Data Incorrect")
            return
        scores.append(team)

    for i in range(n):
        average = sum(scores[i]) / m
        maximum = max(scores[i])
        total += sum(scores[i])
        print(f"Team {i + 1}: Average = {average:.2f}, Max = {maximum}")

    print(f"Total Score of All Teams = {total}")
main()
