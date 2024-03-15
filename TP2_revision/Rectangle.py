class Rectangle:
    def __init__(self,width,height):
        self._width=width
        self._height=height
    def height1(self):
        return self._height
    def width1(self):
        return self._width

    def height(self,val):
        self.set_height(val)
    def width(self,val):
        self.set_width(val)


    def set_width(self,val):
        if val<0 or val>50:
            print("la latgeur n'est pas neg")
        else:
            self._width=val
    def set_height(self,val):
        if val<0 or val>50:
            print("la hauteur n'est pas correcte")
        else:
            self._height = val


    def get_area(self):
        return (self._width * self._height)

    def get_perimeter(self):
        return (self._width + self._height) * 2

    def get_diagonal(self):
        return ((self._width ** 2 + self._height ** 2) ** 0.5)
    def get_picture(self):
        form=""
        for i in range(self._height):
            for j in range(self._width):
                form+="* "
            form+="\n"

        return form
    def get_amount_inside(self,shape):
        return ((self._height//shape._height) *(self._width//shape._width))
    def __str__(self):
        return f"Rectangle(width={self._width}, height={self._height})"






