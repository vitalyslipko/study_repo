class Parallelogram:

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        return f"The area of a parallelogram is {self.width * self.length} cm2"


parallelogram = Parallelogram(5, 10)
print(parallelogram.get_area())


class Square(Parallelogram):

    def get_area(self):
        return f"The area of a square is {self.width ** 2} cm2"


square = Square(5, 10)
print(square.get_area())
