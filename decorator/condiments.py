# condiments.py
# Contiene el Decorador Abstracto y los Decoradores Concretos.

from abc import ABC, abstractmethod
from decimal import Decimal

from beverages import Beverage, Size
from utils import calculate_size_based_cost


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

    def cost(self) -> Decimal:
        size = self._beverage.get_size()
        milk_cost = calculate_size_based_cost(size, "0.10", "0.15", "0.20")
        return self._beverage.cost() + milk_cost


class Mocha(CondimentDecorator):
    """
    Decorador para añadir Mocha a una bebida.
    """

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Mocha"

    def cost(self) -> Decimal:
        size = self._beverage.get_size()
        mocha_cost = calculate_size_based_cost(size, "0.20", "0.25", "0.30")
        return self._beverage.cost() + mocha_cost


class Soy(CondimentDecorator):
    """
    Decorador para añadir Soja a una bebida.
    El costo depende del tamaño de la bebida.
    """

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Soja"

    def cost(self) -> Decimal:
        size = self._beverage.get_size()
        soy_cost = calculate_size_based_cost(size, "0.10", "0.15", "0.20")
        return self._beverage.cost() + soy_cost


class Whip(CondimentDecorator):
    """
    Decorador para añadir Crema a una bebida.
    """

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Crema"

    def cost(self) -> Decimal:
        size = self._beverage.get_size()
        whip_cost = calculate_size_based_cost(size, "0.10", "0.15", "0.20")
        return self._beverage.cost() + whip_cost


class Caramel(CondimentDecorator):
    """
    Decorador para añadir Caramelo a una bebida.
    """

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Caramelo"

    def cost(self) -> Decimal:
        size = self._beverage.get_size()
        caramel_cost = calculate_size_based_cost(size, "0.20", "0.25", "0.30")
        return self._beverage.cost() + caramel_cost


class PrettyDescriptionDecorator(CondimentDecorator):
    """
    Decorador que modifica la descripción para agrupar condimentos repetidos.
    Por ejemplo, convierte "Mocha, Mocha, Whip" en "Double Mocha, Whip".
    """

    def get_description(self) -> str:
        # Obtén la descripción original
        original_description = self._beverage.get_description()

        # Divide los condimentos en una lista
        items = original_description.split(", ")

        # Cuenta las repeticiones de cada condimento
        counts = {}
        for item in items:
            counts[item] = counts.get(item, 0) + 1

        # Reconstruye la descripción agrupando repeticiones
        grouped_description = []
        for item, count in counts.items():
            if count == 1:
                grouped_description.append(item)
            elif count == 2:
                grouped_description.append(f"Double {item}")
            elif count == 3:
                grouped_description.append(f"Triple {item}")
            else:
                grouped_description.append(f"{count}x {item}")

        # Une los elementos agrupados en una nueva descripción
        return ", ".join(grouped_description)

    def cost(self) -> Decimal:
        # No modifica el costo; delega al componente envuelto
        return self._beverage.cost()
