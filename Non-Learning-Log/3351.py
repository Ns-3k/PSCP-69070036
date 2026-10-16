"""3351"""
def main():
    """bnny"""
    text = input().casefold()
    count = 0
    max_count = 0
    if all(ch in "it" for ch in text):
        print(f"unknown {len(text)}")
        return
    for i, ch in enumerate(text):
        if ch == "a":
            if not i or text[i-1] not in "ra":
                print(f"no {i}")
                return
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
        if ch == "r" and (i + 1 == len(text) or text[i+1] != "a"):
            print(f"no {i+1 if i+1 < len(text) else i}")
            return
        if ch == "b" and (i + 1 == len(text) or text[i+1] not in "it"):
            print(f"no {i+1 if i+1 < len(text) else i}")
            return
    print(f"yes {max_count}")
main()
