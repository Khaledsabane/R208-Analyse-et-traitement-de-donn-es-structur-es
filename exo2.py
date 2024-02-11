import sys
import os
if __name__=='__main__':
    def affiche(dossier):
        ''' cette fonction permet d'afficher le contenu d'un fichier '''

        if len(sys.argv)<2:
            print(f"Pas assez d’arguments pour le script ")
        elif os.path.exists(sys.argv[1]):
            os.listdir(sys.argv[1])
            for i in os.listdir(sys.argv[1]):
                print(i)
        else:
            print("fichier non existant")

dossier=sys.argv[1]
affiche(dossier)
help(affiche)
