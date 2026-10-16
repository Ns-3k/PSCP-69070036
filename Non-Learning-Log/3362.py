"""3362"""
def main():
    """vas"""
    name1 = input().casefold()
    name2 = input().casefold()
    name3 = ""
    count = 0
    max_count = 0
    if len(name1) < len(name2):
        name1,name2 = name2,name1
    for i in range (len(name1)-len(name2)):
        name2 += name2[i]
    for ch1,ch2 in zip(name2,name1):
        if ch1 in ("l","o","v","e") or ch2 in ("l","o","v","e"):
            name3 += "w"
            count += 1
            max_count = max(count,max_count)
        else:
            name3 += "$"
            count = 0
    if name3.count("w")%2 == 1:
        name3 += str(max_count)
    else:
        if max_count < 2:
            name3 += "#"
    print(name3)
main()
