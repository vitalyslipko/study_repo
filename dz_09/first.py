class Car:
    def __init__(self, brand, color, volume):
        self.brand = brand
        self.color = color
        self.volume = volume

    def drive_mode(self, a, b):
        self.a = a
        self.b = b

volvo = Car("Volvo", "light blue", "2.5 cm3")
volvo.drive_mode("forward", "backward")
print(f"{volvo.brand} can move {volvo.a} and {volvo.b},in only {volvo.color} color, and volume is {volvo.volume}")

class Vehicle(Car):
    def __init__(Car):
        pass
    def drive_mode(self, rightward, leftward):
        self.rightward = rightward
        self.leftward = leftward

volvo1 = Vehicle()
volvo1.drive_mode("right", "left")
print(f"{volvo.brand} can move {volvo1.rightward} and {volvo1.leftward}, in only {volvo.color} color, and volume is {volvo.volume}")
