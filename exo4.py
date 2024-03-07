import sys, os

ld = []
lf = []
#print(os.environ["Path"])
def recherche(dossier, fichier):
    liste = os.listdir(dossier)
    #print(liste)
    listeFichiers = []
    listeDossiers = []

    for elt in liste:
        if os.path.isfile(f"{dossier}\{elt}") and fichier==elt:
            listeFichiers.append(f"{dossier}\{elt}")
        # elt correspond au fichier à ajouter dans la liste
        # dossier + elt réprésente le chemin complet du dossier
        elif os.path.isdir(f"{dossier}\{elt}") :
            listeDossiers.append(f"{dossier}\{elt}")
            # elt correspond au dossier à ajouter dans la liste
            # dossier + elt réprésente le chemin complet du dossier

    return listeFichiers, listeDossiers

def affiche_contenu(dossier):
    for elt in os.listdir(dossier):
        print(elt)
    return

def affiche2(l):
    for elt in l:
        print(f"     {elt}")
    return

def aide(msg):
    print(msg)
    print(f"Pour utiliser le scripte {os.path.basename(sys.argv[0])} il faut donner un nom de dossier comme argument. Par exemple python {os.path.basename(sys.argv[0])} nom-dossier")

def start_find3():
    if len(sys.argv) <= 1:
        aide("Pas d'argument")
    else:
        if (not os.path.isdir(sys.argv[2])):
            aide("C'est n'est pas un dossier")
        else :
            lf, ld = recherche(sys.argv[2],sys.argv[4])
    for d in ld:
        lf2, ld2 = recherche(d, sys.argv[4])
        lf.extend(lf2)
        ld.extend(ld2)

    print("La liste des fichier est :")
    affiche2(lf)

if __name__ == '__main__':
    start_find3()



