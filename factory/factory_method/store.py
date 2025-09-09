from abc import ABC, abstractmethod
from .pizza import (
    Pizza,
    NYStyleCheesePizza, ChicagoStyleCheesePizza,
    NYStyleVeggiePizza, ChicagoStyleVeggiePizza,
    NYStylePepperoniPizza, ChicagoStylePepperoniPizza,
)

class PizzaStore(ABC):
    def order_pizza(self, kind: str) -> Pizza:
        pizza = self.create_pizza(kind)
        pizza.prepare(); pizza.bake(); pizza.cut(); pizza.box()
        return pizza
    @abstractmethod
    def create_pizza(self, kind: str) -> Pizza: ...

class NYPizzaStore(PizzaStore):
    def create_pizza(self, kind: str) -> Pizza:
        k = kind.lower()
        if k == "cheese":
            return NYStyleCheesePizza()
        elif k == "veggie":
            return NYStyleVeggiePizza()
        elif k == "pepperoni":
            return NYStylePepperoniPizza()
        else:
            raise ValueError(f"No NY pizza for kind: {kind}")

class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, kind: str) -> Pizza:
        k = kind.lower()
        if k == "cheese":
            return ChicagoStyleCheesePizza()
        elif k == "veggie":
            return ChicagoStyleVeggiePizza()
        elif k == "pepperoni":
            return ChicagoStylePepperoniPizza()
        else:
            raise ValueError(f"No Chicago pizza for kind: {kind}")
