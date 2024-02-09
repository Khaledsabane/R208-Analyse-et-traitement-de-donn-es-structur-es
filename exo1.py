import sys
if __name__=='__main__':
    if len(argv)==1:
        print(f"Pas assez d’arguments pour le script nom duscript")
    elif len(argv) > 1:
        for i in range(len(argv)):
            print(sys.argv[i])