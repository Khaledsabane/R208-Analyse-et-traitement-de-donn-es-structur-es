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