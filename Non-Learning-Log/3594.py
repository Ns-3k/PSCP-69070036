"""3594"""
def main():
    """median"""
    num = list(map(float,input().split(",")))
    median = 0
    num.sort()
    if len(num) % 2:
        median = num[int(len(num)/2)]
    else:
        median = (num[int(len(num)/2)-1] + num[int(len(num)/2)])/2
    print(f"{median:.2f}")
main()
