"""3164"""
def main():
    """summmmmmmmmmmm"""
    num = int(input())
    total = 0
    summed = []
    for _ in range(num):
        num1 = int(input())
        num2 = int(input())
        total += max(num1,num2)
        summed.append(max(num1,num2))
    if num == 1:
        print(total)
    else:
        for i in range(num):
            if i != num-1:
                print(summed[i],end=" + ")
            else:
                print(summed[i],end=" = ")
        print(total)
main()
