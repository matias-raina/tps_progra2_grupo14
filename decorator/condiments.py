# condiments.py
# Contiene el Decorador Abstracto y los Decoradores Concretos.

from abc import ABC, abstractmethod

from beverages import Beverage, Size


# --- Decorador Abstracto ---
class CondimentDecorator(Beverage, ABC):
    """
    Clase base para los decoradores de condimentos.
    Hereda de Beverage para tener el mismo tipo.
    Mantiene una referencia a la bebida que está envolviendo.
    """

    def __init__(self, beverage: Beverage):
        self._beverage = beverage

    def set_size(self, size: Size) -> None:
        """
        Propaga la operación de establecer tamaño al componente envuelto.
        """
        self._beverage.set_size(size)

    def get_size(self) -> Size:
        """
        Delega la consulta de tamaño al componente envuelto.
        """
        return self._beverage.get_size()

    @abstractmethod
    def get_description(self) -> str:
        pass


# --- Decoradores Concretos ---
class Milk(CondimentDecorator):
    """
    Decorador para añadir Leche a una bebida.
    """

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Leche"

    def cost(self) -> float:
        return self._beverage.cost() + 0.10


class Mocha(CondimentDecorator):
    """
    Decorador para añadir Mocha a una bebida.
    """

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Mocha"

    def cost(self) -> float:
        return self._beverage.cost() + 0.20


class Soy(CondimentDecorator):
    """
    Decorador para añadir Soja a una bebida.
    El costo depende del tamaño de la bebida.
    """

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Soja"

    def cost(self) -> float:
        # Costo base de la bebida
        base_cost = self._beverage.cost()

        # Costo de soja según tamaño
        size = self._beverage.get_size()
        if size == Size.TALL:
            soy_cost = 0.10
        elif size == Size.GRANDE:
            soy_cost = 0.15
        elif size == Size.VENTI:
            soy_cost = 0.20
        else:
            soy_cost = 0.15  # Fallback por si acaso

        return base_cost + soy_cost


class Whip(CondimentDecorator):
    """
    Decorador para añadir Crema a una bebida.
    """

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Crema"

    def cost(self) -> float:
        return self._beverage.cost() + 0.10


class Caramel(CondimentDecorator):
    """
    Decorador para añadir Caramelo a una bebida.
    """

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Caramelo"

    def cost(self) -> float:
        return self._beverage.cost() + 0.20
