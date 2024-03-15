from Rectangle import Rectangle
from Carre import Carre
if __name__=="__main__":
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.height(3)
    print(rect.get_perimeter())

    print(rect)
    print(rect.get_picture())

    sq = Carre(9)
    print(sq.get_area())
    sq.side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())
    rect.height(8)
    rect.width (16)

    print(rect.get_amount_inside(sq))



