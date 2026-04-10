class circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        a = 3.14 * self.r * self.r
        print("the area of the circle is", a)

    def perimeter(self):
        p = 2 * 3.14 * self.r
        print("the perimeter of the circle is", p)

c1 = circle(7)
c1.area()
c1.perimeter()
