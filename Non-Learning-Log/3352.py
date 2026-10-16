"""3352"""
import json
def main():
    """last"""
    temp = input()
    numlist = json.loads(temp)
    for i in numlist:
        print(f"{str(i)[-1]}")
main()
