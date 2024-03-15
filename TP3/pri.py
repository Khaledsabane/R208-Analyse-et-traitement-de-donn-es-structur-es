from film import film
from bibliotheque import bibliotheque
if __name__=="__main__":
    movie1 = film("Gladiator", "2003", "9")
    movie1.ajouter_avis("Parfait")
    movie1.ajouter_avis("nul")

    movie2 = film("HERES", "2001", "10")
    movie2.ajouter_avis("Parfait")
    movie2.ajouter_avis("nul")

    movie3 = film("GOT", "2010", "8")
    movie3.ajouter_avis("Parfait")
    movie3.ajouter_avis("nul")

    movie4 = film("LUPIN", "2010", "8")
    movie4.ajouter_avis("Parfait")
    movie4.ajouter_avis("nul")


    print(movie1)
    print(movie1.afficher_avis())

    biblio = bibliotheque()

    # Ajoutez les films à la bibliothèque en utilisant la méthode d'instance 'ajouter_film'
    biblio.ajouter_film(movie1)
    biblio.ajouter_film(movie2)
    biblio.ajouter_film(movie3)
    biblio.ajouter_film(movie4)

    # Appelez la méthode d'instance 'mostrate' pour afficher le meilleur film
    biblio.mostrate()
    biblio.lastmovie()
    biblio.avrgnote()
    biblio.top3()


