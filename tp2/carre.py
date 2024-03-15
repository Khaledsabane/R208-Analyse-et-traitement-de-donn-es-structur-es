from Rectangle import Rectangle
class Carree(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)

    def set_side(self,s):
        self.height=s
        self.width=s


    def set_height (self,s):
        self.height=self

    def  set_width(self,s):
        self.width = self
    def __str__(self):
        return f"Carree(side={self.width})"
----------------------------------------------------------------------------
from Rectangle import Rectangle

class Carre(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)
        self.__side=side

    def get_side(self):
        return self.height

    def set_side(self, side):
        if side < self.MIN_HEIGHT:
            print("Attention une valeur négative du side a été donnée !")
        else:
            self.width = side
            self.height = side

    #def get_picture(self, etoile="* "):
    #    return super().get_picture(etoile)

    def __str__(self):
        return f"{self.__class__.__name__}'(side={self.width})"

    side = property(fget=get_side, fset=set_side)



if __name__ == "__main__":
    print("Tests unitaires de la classe Carre")
    rect = Rectangle(10, 5)
    print(rect)
    print("l'aire du rectangle est : ", rect.get_area())
    rect.height = 3
    #print("rect : ", rect)
    print("le périmètre du rectangle est : ", rect.get_perimeter())

    print(rect.get_picture())

    sq = Carre(9)
    print(sq)
    #print("sq : ", sq)
    print("l'aire du carrée est : ", sq.get_area())
    sq.side = 4
    print("la diagonale est :", sq.get_diagonal())
    print(sq)
    print(sq.get_picture())
    rect.height = 8
    rect.width = 16
    print(rect)
    print(f"Il est possible de placer {rect.get_amount_inside(sq)} carrées ({sq}) dans le rect ({rect})")
    #print(type(sq.side))
