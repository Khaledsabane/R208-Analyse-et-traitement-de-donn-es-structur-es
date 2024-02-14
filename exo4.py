import sys, os
def recherche(dossier, fichier):
    liste = os.listdir(dossier)
    listeFichiers = []
    listeDossiers = []


    for elt in liste:
        chemin = os.path.join(dossier, elt)
        if os.path.isfile(chemin):
            if elt==fichier:

                listeFichiers.append(chemin)

        elif os.path.isdir(chemin):

            listeDossiers.append(chemin)

    for p in listeDossiers:
        recherche(p,fichier)
    for i in listeFichiers:
        print(f"      {i}")


if __name__== '__main__':
    dossier=sys.argv[1]
    fichier=sys.argv[2]
    recherche(dossier,fichier)