"""3482"""
def attack(name, secret):
    """fight"""
    print(name)
    attempt = 0
    while attempt < 2:
        try:
            guess = int(input())
        except EOFError:
            return False, attempt, True
        attempt += 1
        if guess == secret:
            print("kill")
            return True, attempt, False
    print("back")
    return False, attempt, False

def main():
    """sdasdad"""
    demons = {
        "Spider Demon": 1,
        "Swamp Demon": 2,
        "Arrow Demon": 1,
        "Hand Demon": 2,
        "Drum Demon": 3,
        "Mugen Train": 2,
        "Upper Moon": 3
    }
    total_attack = 0
    killed = set()
    out_of_input = False
    while len(killed) < 5 and not out_of_input:
        for name, secret in demons.items():
            if name in killed:
                continue
            success, attempt, out_of_input = attack(name, secret)
            total_attack += attempt
            if success:
                killed.add(name)
            if len(killed) == 5 or out_of_input:
                break
    print(total_attack)
main()
