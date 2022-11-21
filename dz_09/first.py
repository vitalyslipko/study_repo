class Car:
    def __init__(self, brand, color, volume):
        self.brand = brand
        self.color = color
        self.volume = volume

    def forward(self):
        return "forward"

    def backward(self):
        return "backward"

volvo = Car("Volvo", "light blue", "2.5 cm3")
print(volvo.brand)
# volvo.forward()
print(f"The {volvo.brand} can move {volvo.forward()} and {volvo.backward()}, only {volvo.color} color is available at the moment, and {volvo.volume} volume is only available")

class Vehicle:
    def __init__(Car):
        pass
    def turn_left(self):
        return "left"
    def turn_right(self):
        return "right"

volvo1 = Vehicle()
print(f"The {volvo.brand} can move {volvo1.turn_right()} and {volvo1.turn_left()}, only {volvo.color} color is available at the moment, and {volvo.volume} volume is only available")
