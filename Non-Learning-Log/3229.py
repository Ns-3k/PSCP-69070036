"""3229"""
def main():
    """score calc"""
    base = int(input())
    bonus = int(input())
    days = int(input())
    score = base+bonus
    if days > 3:
        score = score * 1.5 // 1
    if score >= 1500:
        rank = 5
    elif score >= 1000:
        rank = 4
    elif score >= 500:
        rank = 3
    elif score >= 200:
        rank = 2
    else:
        rank = 1
    if rank == 5 and days >= 7:
        special = 99
    elif rank == 4 and bonus > 300:
        special = 88
    else:
        special = 0
    if not score % 1:
        print(f"{int(score)}\n{rank}\n{special}")
    else:
        print(f"{score}\n{rank}\n{special}")
main()
