class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, l):
        self.length = l
    def area(self):
        a = self.length * self.length
        return a
s = Square(int(input()))
print(s.area())