import os,sys
lf=[]
ld=[]
def recherche(dossier):
    liste = os.listdir(dossier)

    listeFichiers=[]
    listeDossiers=[]

    for elt in liste :

        if  os.path.isfile(f"{dossier}\{elt}") :
             listeFichiers.append(f"{dossier}\{elt}")


             # elt correspond au dossier à ajouter dans la

             # ‘dossier + elt’ réprésente le chemin complet sur le fichier
        elif os.path.isdir(f"{dossier}\{elt}"):
             listeDossiers.append(f"{dossier}\{elt}")
    return listeFichiers, listeDossiers

def affiche(l):
    for e in l:
        print(e)
    return

def start_find2():
    lf,ld =recherche(sys.argv[1])
    for i in ld:
        lf2,ld2=recherche(i)
        lf.extend(lf2)
        ld.extend(ld2)
    print(f"la liste des dossiers :")
    affiche(ld)
    print(f"la liste des fichiers :")
    affiche(lf)





if __name__=='__main__':
    start_find2()

