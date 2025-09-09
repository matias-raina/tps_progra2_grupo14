from abc import ABC, abstractmethod

class Pizza(ABC):
    name: str = "Generic Pizza"
    toppings: list[str] = []

    def prepare(self):
        print(f"Preparing {self.name}")
        print("Adding toppings:", ", ".join(self.toppings))

    def bake(self): print("Bake 25 min at 350")
    def cut(self):  print("Cutting pizza into diagonal slices")
    def box(self):  print("Place pizza in official box")
    def __str__(self): return self.name

class NYStyleCheesePizza(Pizza):
    def __init__(self):
        self.name="NY Style Sauce & Cheese"; self.toppings=["Reggiano cheese"]

class NYStyleVeggiePizza(Pizza):
    def __init__(self):
        self.name='NY Style Veggie Pizza' ; self.toppings=[''] ; self.toppings = ["Mushroom", "Onion", "Red Pepper"]

class NYStylePepperoniPizza(Pizza):
    def __init__(self):
        self.name = "NY Style Pepperoni Pizza" ; self.toppings = ["Sliced Pepperoni", "Onion", "Cheese"]

class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        self.name="Chicago Style Deep Dish Cheese"; self.toppings=["Shredded Mozzarella"]
    def cut(self): print("Cutting the pizza into square slices")

class ChicagoStyleVeggiePizza(Pizza):
    def __init__(self):
        self.name = "Chicago Style Veggie Pizza" ; self.toppings = ["Mushroom", "Onion", "Red Pepper", "Olives"]

    def cut(self): print("Cutting the pizza into square slices")

class ChicagoStylePepperoniPizza(Pizza):
    def __init__(self):
        self.name = "Chicago Style Pepperoni Pizza" ; self.toppings = ["Sliced Pepperoni", "Onion", "Shredded Mozzarella"]

    def cut(self): print("Cutting the pizza into square slices")