class Voiture:
    def __init__(self,marque='X',modele='s-line',puissance_Fiscale='3',couleur='Noir'):
        self.__marque=marque
        self.__modele=modele
        self.__puissance_Fiscale=puissance_Fiscale
        self.__couleur=couleur
        self.__option = []
    def getmarque(self):
        return self.__marque
    def getmodele(self):
        return self.__modele
    def getpuissance(self):
        return self.__puissance_Fiscale
    def getcouleur(self):
        return self.__couleur
    def getoption(self):
        return self.__option


    def setmarque(self,m):
        self.__marque=m
    def setmodele(self,m):
        self.__modele=m
    def setpuissance(self,m):
        self.__puissance_Fiscale=m
    def setcouleur(self,m):
        self.__couleur=m
    def setoption(self,m):
        self.__option=m


    def ajouter_option(self, opts) :
        self.__option.append(opts)
    def supprimer_option(self, opts):
        self.__option.remove(opts)
    def is_option_present(self, opt):
        return opt in self.__option



    def __str__(self):
        return f"Voici les caractéristiques de cette voiture: \n -Marque : {self.__marque} \n- Modele : {self.__modele} \n - Couleur : {self.__couleur} \n - puissance : {self.__puissance_Fiscale} \n- options : {self.__option}"

