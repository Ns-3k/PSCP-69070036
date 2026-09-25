"""3160"""
def main():
    """prime"""
    start,stop = map(int,input().split(" "))
    allprime = []
    prime = True
    for i in range (start,stop+1):
        if i > 1:
            prime = True
            for j in range(2, int(i**0.5) + 1):
                if not i%j:
                    prime = False
                    break
            if prime:
                allprime.append(i)
    if allprime:
        print(*allprime)
    print("Total primes:",len(allprime))
main()
