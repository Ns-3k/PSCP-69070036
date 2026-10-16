"""3476"""
import json
def main():
    """cat"""
    n = int(input())
    cats = {"Garfield": "Cat01"}
    foxes = {"Fubuki": "Fox01"}
    for _ in range(n):
        temp = json.loads(input())
        for name, kind in temp.items():
            cats.pop(name, None)
            foxes.pop(name, None)
            if kind.startswith("Cat"):
                for cat_name, cat_kind in list(cats.items()):
                    if cat_kind == kind:
                        del cats[cat_name]
                for fox_name, fox_kind in list(foxes.items()):
                    if fox_kind == "Cat01" and name != "Garfield":
                        del foxes[fox_name]
                cats[name] = kind
            else:
                for fox_name, fox_kind in list(foxes.items()):
                    if fox_kind == kind:
                        del foxes[fox_name]
                foxes[name] = kind
    print("Cat :",len(cats))
    print("Fox :",len(foxes))
    for name, kind in sorted(cats.items(), key=lambda x: int(x[1][3:])):
        print(name ,":",kind)
    for name, kind in sorted(foxes.items(), key=lambda x: int(x[1][3:])):
        print(name, ":",kind)
main()
