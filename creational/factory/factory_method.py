from abc import ABC, abstractmethod


# Abstract Product
class Animal(ABC):
    @abstractmethod
    def speak(self): ...


# Concrete Products
class Dog(Animal):
    def speak(self):
        print("Bhow Bhow")


class Cat(Animal):
    def speak(self):
        print("Meow Meow")


class Cow(Animal):
    def speak(self):
        print("Moo Moo")


# AbstractFactory
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self) -> Animal: ...


# Concrete Factory Classes
class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()


class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()


class CowFactory(AnimalFactory):
    def create_animal(self):
        return Cow()


# Driver code.
def animal_narrator(factory: AnimalFactory):
    animal = factory.create_animal()
    animal.speak()


animal_narrator(CatFactory())
animal_narrator(DogFactory())
