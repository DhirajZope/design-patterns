# To implement abstract factory pattern we need following things.
# 1. Abstract class of the functionality
# 2. Concrete classes of the functionality
# 3. Abstract factory class
# 4. Factory class that manages these factories.
#
# Use this pattern of you want to create family of objects.

from abc import ABC, abstractmethod


# Abstract Functionality classes
class Button(ABC):
    @abstractmethod
    def click(self): ...


class TextBox(ABC):
    @abstractmethod
    def insert(self, text): ...


# Concrete Functionality classes
class WindowsButton(Button):
    def click(self):
        print("Windows button clicked")


class MacButton(Button):
    def click(self):
        print("Mac button is clicked")


class WindowsTextBox(TextBox):
    def insert(self, text):
        print(f"Win Typed:  {text}")


class MacTextBox(TextBox):
    def insert(self, text):
        print(f"Mac Typed:  {text}")


# Abstract Factory Class
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button: ...

    @abstractmethod
    def create_textbox(self) -> TextBox: ...


# Concrete Factory Classes
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_textbox(self):
        return WindowsTextBox()


class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_textbox(self):
        return MacTextBox()


# Create Factory of Factory
class GUIToolKit:
    factory = {"win": WindowsFactory, "mac": MacFactory}

    @classmethod
    def create_toolkit(cls, type):

        if type in cls.factory:
            return cls.factory[type]()

        raise ValueError("Platform not supported.")


# Driver code
toolkit = GUIToolKit.create_toolkit("mac")
button = toolkit.create_button()
text_box = toolkit.create_textbox()

button.click()
text_box.insert("This is my world")
