"""3226"""
from decimal import Decimal, ROUND_DOWN, getcontext
def main():
    """inflation"""
    getcontext().prec = 10000
    n = Decimal(input())
    k = int(input())
    rate = Decimal("0.0381")
    for _ in range(k):
        n += (n * rate).quantize(Decimal("0.01"),rounding=ROUND_DOWN)
    print(n.quantize(Decimal("0.01"),rounding=ROUND_DOWN))
main()
