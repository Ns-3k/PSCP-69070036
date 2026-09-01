"""3156"""
def main():
    """conan"""
    text = input()
    code = int(input())
    cipher = ""
    for ch in text:
        if ord(ch) + code%26 > 122:
            cipher += chr(ord(ch) + code%26 - 26)
        else:
            cipher += chr(ord(ch) + code%26)
    print(cipher)
main()
