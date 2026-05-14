#14 may 26

class Temperature:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f"{self.value:.1f} C"

    def to_fahrenheit(self):
        fahrenheit = (self.value * 9/5) + 32
        return f"{fahrenheit} F"
    
    @classmethod
    def from_fahrenheit(cls, f):
        celsius = (f - 32) * 5/9
        return cls(celsius)

    @classmethod
    def from_kelvin(cls, k):
        celsius = k - 273.15
        return cls(celsius)
    
    @staticmethod
    def is_valid(celsius):
        return celsius > -273.15
    

t1 = Temperature(30)
print(t1)
print(t1.to_fahrenheit())

t2 = Temperature.from_fahrenheit(86)
print(t2)
t3 = Temperature.from_kelvin(300)
print(t3)

print(Temperature.is_valid(-300))
print(Temperature.is_valid(23))