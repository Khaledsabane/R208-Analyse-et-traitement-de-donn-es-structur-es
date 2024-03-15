from Rectangle import Rectangle

class Carre(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)
    def side(self,val):
         self.set_side(val)



    def set_side(self,s):
        self._height=s
        self._width=s



    def __str__(self):
        return f"Carree(side={self._width})"