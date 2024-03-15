import sys
if __name__=='__main__':
    if len(sys.argv)>1:
        for i in range(len(sys.argv)):
            print(f"         =>{sys.argv[i]}")

    else:
        print(f"Pas assez d'arguments")
