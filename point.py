import cmath        
import math
class Point:
    def __init__(self,x,y=None):
        if isinstance(self, x, Point):

          self.x=x.x
          self.y=y.y
        else:
            self.x=x
            self.y=y
              
        def __str__(self):
            return f"({self.x},{self.y})"
        def __getitem__(self,i):
            if i==0:
                return self.x
            if i==1:
                return self.y
            else:
                raise IndexError("Index out of range. Use 0 for x and 1 for y.")
        def __str__(self):
            return f"({self.x}, {self.y})"
        def __eq__(self,orther):
            return isinstance(orther, Point) and self.x==orther.x and self.y==orther.y
        def angle(self,p):
            
p1=Point(1,2) 
p2=Point(3,4)
print(p)
        
         #ajout de la methode pour vevifier si deux sont égaux
         
         
        
        
