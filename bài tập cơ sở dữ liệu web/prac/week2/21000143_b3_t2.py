#class point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # method to print point
    def print_point(self):
        print("Point(%s, %s)" % (self.x, self.y))
    
    # method to calculate distance between two points
    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
    
#test
p1 = Point(1, 2)
p2 = Point(3, 4)
p1.print_point()
p2.print_point()
print("Distance of 1st point and 2nd point is:",p1.distance(p2))