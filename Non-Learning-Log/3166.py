"""3166"""
def main():
    """pass or not"""
    subject = int(input())
    status = "PASS"
    total = 0
    for _ in range (subject):
        score = int(input())
        if score < 50:
            status = "FAIL"
        total += score
    if total/subject < 60:
        status = "FAIL"
    print(f"{total/subject:.1f}\n{status}")
main()
