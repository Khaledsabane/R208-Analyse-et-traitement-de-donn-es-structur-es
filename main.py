from Voiture import Voiture
if __name__=="__main__":
    myCar1=Voiture("Opel","Clio","2")
    myCar2=Voiture()
    myCar3=Voiture("Model S", "Tesla","5")
    myCar4=Voiture(couleur='Rouge')
    print(f"Voiture {myCar1.getmarque()}")

    myCar1.setmarque('BMW')
    myCar2.setmarque('COROLLA')
    myCar1.__str__()
    myCar2.__str__()
    print(f"Voiture {myCar1}")
    print(f"Voiture {myCar2}")
    myCar1.ajouter_option('autoparking')
    myCar1.ajouter_option('autodriving')
    myCar1.supprimer_option('autoparking')
    print(f"Voiture {myCar1}")

print(f"Resultat de la recherche : {myCar1.is_option_present('autoparking')}")

