class Shape:

    def __init__(self, length, breadth):
        self.length=length
        self.breadth=breadth

class Rectangle(Shape):

        def __init__(self,length, breadth):
             Shape.__init__(self, length, breadth)
        def calculate(self):
             
             area=self.length*self.breadth
             print(area)

obj=Rectangle(450, 600)
obj.calculate()





             
             
        

        
       
        
             

