# 28 june 26

from abc import ABC , abstractmethod
import math


class Shape(ABC):
	
 @abstractmethod
 def area(self):
  pass
  
 @abstractmethod
 def perimeter(self):
  pass
	
 @abstractmethod
 def describe(self):
  pass
  
  
class Circle(Shape):
 def __init__(self, radius):
  self.radius = radius
  
 def area(self):
  return math.pi * self.radius**2
  
 def perimeter(self):
  return 2 * math.pi * self.radius
  
 def describe(self):
  return f"Circle with {self.area():.2f} area and {self.perimeter():.2f} perimeter"
  
class Triangle(Shape):
 def __init__(self, a, b, c):
  self.a, self.b, self.c = a, b, c
  
 def area(self):
  s = self.perimeter() / 2
  return math.sqrt(s * (s - self.a)*(s - self.b)*(s - self.c))
  
 def perimeter(self):
  return self.a + self.b + self.c
  
 
 def describe(self):
    return f"Triangle — sides: {self.a}, {self.b}, {self.c} | area: {self.area():.2f}, perimeter: {self.perimeter():.2f}"
  
class Rectangle(Shape):
 def __init__(self, length, width):
  self.length, self.width = length, width
  
 def area(self):
  return self.length * self.width
  
 def perimeter(self):
  return 2 * (self.length + self.width)
  
 def describe(self):
  return f"Rectangle with {self.area():.2f} area and {self.perimeter():.2f} perimeter"
  

class Canvas:
 def __init__(self):
  self.shapes = []
  
 def add_shape(self, shape):
  self.shapes.append(shape)
  
 def total_area(self):
  return sum(shape.area() for shape in self.shapes)
  
 def show_all(self):
  for shape in self.shapes:
   print(shape.describe())



c = Circle(5)
r = Rectangle(4, 6)
t = Triangle(3, 4, 5)  # three sides; think about area formula

canvas = Canvas()
canvas.add_shape(c)
canvas.add_shape(r)
canvas.add_shape(t)

canvas.show_all()
print(canvas.total_area())