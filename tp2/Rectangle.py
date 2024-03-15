class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def width(self):
        return self.width
    def heigh(self):
        return self.height
    def width(self,value):
        self.set_width(value)
    def height(self,value):
        self.set_height(value)


    def set_height(self,value):
        if value < 0:
            print("la hauteur n'est pas neg")
        else:
            self.height = value

    def set_width(self,value):
        if value < 0:
            print("la largeur n'est pas neg")
        else:
            self.width = value


    def get_perimeter(self):
        return (self.width+self.height)*2
    def get_area(self):
        return (self.width*self.height)
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** 0.5)
    def get_picture(self):

        if self.width > 50 or self.height>50:
            return f"trop grand"
        else:
            form = ""
            for h in range(self.height):
                for w in range(self.width):
                    form += "*  "
                form += "\n"
            return form
    def get_amount_inside(self, shape):
        return (self.width//shape.width)*(self.height//shape.height)






    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
-------------------------------------------------------------
class Rectangle:
    TAILLE_ECRAN = 50
    MIN_WIDTH = 1
    MIN_HEIGHT = 1

    def __init__(self, w, h):

        self.__width = w
        self.__height = h

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def set_width(self, w):
        if w < self.MIN_WIDTH:
            print("Attention, une largueur négative ou nulle a été donnée !")
            self.__width = 1
        else:
            self.__width = w

    def set_height(self, h):
        if h < self.MIN_HEIGHT:
            print("Attention, une hauteur négative ou nulle a été donnée !")
            self.__height = 1
        else:
            self.__height = h

    def get_area(self):
        area = self.__width * self.__height
        return area

    def get_perimeter(self):
        perimeter = (self.__width + self.__height) * 2
        return perimeter

    def get_diagonal(self):
        diagonal = ((self.__width ** 2 + self.__height ** 2) ** .5)
        return diagonal

    def get_picture(self, etoile="* "):
        dessin = ""
        if self.__width < self.TAILLE_ECRAN and self.height < self.TAILLE_ECRAN:
            ligne = etoile * self.__width
            for x in range(self.__height):
                dessin += ligne
                if x < self.__height - 1:
                    dessin += "\n"
        else:
            print("Trop grand pour faire une image")
        return dessin

    def get_amount_inside(self, formeatester):
        nbHauteur = self.__height // formeatester.height
        nbLargeur = self.__width // formeatester.width
        return nbHauteur * nbLargeur # nbr de fois qu'on peut avoir la forme 'formeatester' dans l'instance en cours

    def __str__(self):
        return f"{type(self).__name__}'(width={self.__width}, height={self.__height})"

    width = property(fget=get_width, fset=set_width)
    height = property(fget=get_height, fset=set_height)


if __name__ == "__main__":
    print("Tests unitaires de la classe Rectangle")
    rect = Rectangle(10, 5)
    print(rect)
    print("L'aire est : ", rect.get_area())
    rect.height = 3
    print(rect)
    print("le périmètre est : ", rect.get_perimeter())

    print(rect.get_picture('*'))
    #print(dir(rect))

