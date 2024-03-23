import math

class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Rectangle(Shape):
    def init(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def init(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Animal:
    def init(self, name, sound):
        self.name = name
        self.sound = sound

class Dog(Animal):
    def init(self, name):
        super().init(name, "Au")

class Cat(Animal):
    def init(self, name):
        super().init(name, "Meow")

class Cow(Animal):
    def init(self, name):
        super().init(name, "Moo")
