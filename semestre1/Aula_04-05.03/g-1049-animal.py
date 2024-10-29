p1 = input()
p2 = input()
p3 = input()

if p1 == "vertebrado":
    if p2 == "ave":
        if p3 == "carnivoro":
            print("aguia")
        elif p3 == "onivoro":
            print("pomba")
    elif p2 == "mamifero":
        if p3 == "herbivoro":
            print("vaca")
        elif p3 == "onivoro":
            print("homem")

elif p1 == "invertebrado":
    if p2 == "inseto":
        if p3 == "hematofago":
            print("pulga")
        elif p3 == "herbivoro":
            print("lagarta")
    elif p2 == "anelideo":
        if p3 == "hematofago":
            print("sanguessuga")
        elif p3 == "onivoro":
            print("minhoca")