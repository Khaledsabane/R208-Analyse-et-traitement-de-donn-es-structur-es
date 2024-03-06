import os,sys
def affiche(dossier):
    ''' cette fonction permet d'afficher le contenu d'un fichier '''
    for i in os.listdir(dossier):
        print(f"{i}")
def aide(msg):
    ''' cette fonction permet d'afficher les erreurs'''
    print(msg)

def start_find1():
    '''  fonction permet l'affichage du programme  '''
    if len(sys.argv)=<1:
        aide("Pas assez d'arguments")
    else:
        if  os.path.exists(sys.argv[1]):
            print(f"le dossier {sys.argv[1]} existe")
            affiche(sys.argv[1])
        else:
            aide("fichier non existant")


if __name__=='__main__':
    start_find1()




