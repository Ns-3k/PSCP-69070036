"""หาร10"""
def main():
    """asdasd"""
    num=int(input())
    num_checkzero=num%10
    result=num-num_checkzero
    j=result/10
    j=int(j)
    for _ in range(j+1) :
        print (result,end=" ")
        result=result-10
main()
