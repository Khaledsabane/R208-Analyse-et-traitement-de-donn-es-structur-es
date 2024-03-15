from film import film
class bibliotheque:
    def __init__(self):
        self.liste_des_films=[]
    def ajouter_film(self,film):
        return self.liste_des_films.append(film)
    def get_note(self,film):
        return film.note


    def afficher_films(self):
        for i in self.liste_des_films:
            print(f"     - {i}")

    def mostrate(self):
        max_note=0
        top_film=None
        for film in self.liste_des_films:
            if film.note>max_note:
                max_note=film.note
                top_film=film
        if top_film:
            print(f"Le meilleur film est : {top_film.titre}")

    def top3(self):
        self.liste_des_films.sort(key=lambda x: x.note, reverse=True)
        print("Top 3 des films les mieux notés :")
        for i in range(min(3, len(self.liste_des_films))):
            print(self.liste_des_films[i].titre)

    def lastmovie(self):
        last_date=0
        last_film=None
        for film in self.liste_des_films:
            if film.date>last_date:
                last_date=film.date
                last_film=film
        if last_film:
            print(f"Le dernier film est : {last_film.titre}")

    def avrgnote(self):
        somme=0
        nb=0
        moyenne=1
        for film in self.liste_des_films:
            somme+=film.note
            nb+=1
        moyenne=somme/nb
        print(f"La note moyenne de l'ensemble des films de la bibliothèque est : {moyenne:.2f}")







    # Exemple d'utilisation






