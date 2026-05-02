# Design patterns
There are three types of design patterns
1. Creational
2. Structural
3. Behavioural

### Creational Design patterns
- Abstract Factory
- Builder
- Factory Method
- Prototype
- Singleton

### Structural patterns
- Adapter
- Bridge
- Composite
- Decorator
- Facade
- Flyweight
- Proxy

### Behavioural patterns
- Chain of responsibility
- Command
- Interpreter
- Interator
- Mediator
- Memento
- Observer
- State
- Strategy
- Template Method
- Visitor

## Creational Design patterns
Creational design patterns are category of design patterns that deals with how objects are created in a program.
Instead of creating objects directly using constructors everywhere, these patterns provide more flexible and more
controlled ways to instantiate objects.

### Factory Design Pattern.
The factory pattern is a creational design pattern that provides an interface for creating objects, but lets classes
and subclasses decide which class to instantiate.

> Problem it solves
Instead of doing this everywhere:

```python
car = BMW() # Tightly coupled
```

You do:
```python
car = CarFactory.create("BMW")
```
 Now your code:

- is loosely coupled
- doesn’t depend on concrete classes
- is easier to extend

There are three types of factory design patterns.
1. Simple Factory - A Simple Factory is just a class with a method that returns different objects based on input.
2. Abstract Factory - Provides an interface for creating families of related objects without specifying their concrete classes.
3. Factory Method. - Defines an interface for creating objects, but lets subclasses decide which class to instantiate. 
