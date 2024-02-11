import sys
import os


def recherche(dossier):
    liste = os.listdir(dossier)
    listeFichiers = []
    listeDossiers = []

    print(liste)
    for elt in liste:
        chemin = os.path.join(dossier, elt)
        if os.path.isfile(chemin):
            listeFichiers.append(dossier + elt)
            # elt correspond au dossier à ajouter dans la liste
        # ‘dossier + elt’ réprésente le chemin complet sur le fichier
        elif os.path.isdir(chemin):
            listeDossiers.append(dossier + elt)
    print(f"les fichier: {listeFichiers}")
    print(f"les dossiers: {listeDossiers}")
    
if __name__== '__main__':
    dossier=sys.argv[1]
    recherche(dossier)