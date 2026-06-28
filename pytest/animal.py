class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.adopted = False

    def describe(self):
        status = "Adopted" if self.adopted else "Available"
        print(f"Name: {self.name}, Age: {self.age}, Status: {status}")

    def adopt(self):
        self.adopted = True
        print(f"{self.name} has been adopted.")

    def __str__(self):
        return f"{self.name} ({self.__class__.__name__})"

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def describe(self):
        status = "Adopted" if self.adopted else "Available"
        print(f"Dog -> Name {self.name}, Age: {self.age}, "
              f"Breed: {self.breed}, Status: {status}"
              )

class Cat(Animal):
    def __init__(self, name, age, indoor_only):
        super().__init__(name, age)
        self.indoor_only = indoor_only

    def describe(self):
        status = "Indoor Only" if self.indoor_only else "Can stay outdoors"
        adopt_status = "Adopted" if self.adopted else "Available"
        print(f"Cat -> Name: {self.name}, Age: {self.age},"
              f"{status}, status: {adopt_status}"
              )
        
class Shelter:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} added to shelter")

    def show_available(self):
        print("\nAvailable Animals")
        available = False
        for animal in self.animals:
            if not animal.adopted:
                animal.describe()
                available = True
        
        if not available:
            print("No available animals")
    
    def adopt_animal(self, name):
        for animal in self.animals:
            if animal.name.lower() == name.lower():
                if not animal.adopted:
                    animal.adopt()
                else:
                    print(f"{animal.name} is already adopted")
                return
            
        print("Animal not found.")


shelter = Shelter()

dog1 = Dog("bingo",5, "german")
dog1.describe()
cat = Cat("kiddy", 3, True)
cat.describe()
dog2 = Dog("Tim", 4, "US")
dog2.describe()

shelter.add_animal(dog1)
shelter.add_animal(dog2)
shelter.add_animal(cat)

shelter.show_available()

print("\nAdopting kiddy...\n")
shelter.adopt_animal("Kiddy")

shelter.show_available()

print(cat)

