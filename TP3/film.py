class film:
    def __init__(self,titre, date_de_sortie, note):
        self.titre=titre
        self.date=int(date_de_sortie)
        self.note=int(note)
        self.liste_des_avis=[]

    def ajouter_avis(self,f):
        return self.liste_des_avis.append(f)
    def afficher_avis(self):
        for i in self.liste_des_avis:
            print(f"     - {i}")



    def __str__(self):
        return f"le film {self.titre} est sortie le {self.date} , il a la note {self.note} et \nvoici les avis du public l'ayant vu : "
movie1=film("Gladiator", "2003","9")
movie1.ajouter_avis("Parfait")
movie1.ajouter_avis("nul")


