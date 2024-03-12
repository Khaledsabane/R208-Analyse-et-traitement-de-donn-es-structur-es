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