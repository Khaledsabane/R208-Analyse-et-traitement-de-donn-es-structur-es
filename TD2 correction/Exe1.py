def devise1(a,b):
    return a/b

def devise2(a,b):
    if b == 0:
        print("Erreur, b est égale à 0 et on ne peut pas diviser par zéro " \
               "La division n’est pas possible dans ce cas")
    else:
        return a/b


def devise3(a,b):
    try:
        a = int(a)
        b = int(b)
        c= a/b
    except ZeroDivisionError as err:
        print(f"Erreur de type {err}. Donc La division n’est pas possible dans ce cas")
    except ValueError as err:
        print(f"Erreur de type {err}. il faut donner que des entiers ou réels")
    else:
        return a/b

