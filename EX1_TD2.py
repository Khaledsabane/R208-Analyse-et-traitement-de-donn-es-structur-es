import sys


def divise1(a : float, b : float) -> float:
    c = a / b
    return c
def divide2(a,b):
    if b!=0:
        c = a / b
    else:
        print("division par zéro")

def divide3(a,b):
    try:
        c = a / b
    except ZeroDivisionError as e:
        print(f" {e}")
        c = "erreur"
    except ValueError as p:
        print({p})


    else:
         return c


def main():
    flag=False
    while(not flag):
        try:
            a=float(input("saisir a:"))
        except ValueError:
            print("saisir une valeur réelle")
        else:
            flag=True
    flag=False
    while (not flag):
        try:
            b=float(input("saisir b:"))
        except ValueError:
            print("saisir une valeur réelle")
        else:
            flag=True

    c = divide3(a,b)

    if c is not None:
            print(f"affiche la division de {a} par {b} donne {c}")
if __name__=="__main__":
         sys.exit((main()))








#ZeroDivisionError