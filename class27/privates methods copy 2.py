class Point:
     def __init__(self,x=0,y=0):
          self.x = x
          self.y  = y

     def __str__(self):
           return "({0},{1})".format(self.x, self.y)

among = Point(6,7)
print(among)
          


   
