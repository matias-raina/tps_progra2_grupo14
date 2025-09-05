# beverages.py
# Contiene el Componente y los Componentes Concretos del patrón.

from abc import ABC, abstractmethod
from decimal import Decimal
from enum import Enum


# --- Enumeración de Tamaños ---
class Size(Enum):
    """
    Enumeración para los tamaños de bebidas disponibles en Starbuzz.
    """

    TALL = "Tall"
    GRANDE = "Grande"
    VENTI = "Venti"


# --- Componente Abstracto ---
class Beverage(ABC):
    """
    La clase base para todas las bebidas. Utiliza el módulo abc para
    definir que es una clase abstracta.
    """

    def __init__(self):
        self.description = "Bebida Desconocida"
        self._size = Size.TALL  # Tamaño por defecto

    def get_description(self) -> str:
        """
        Devuelve la descripción de la bebida.
        """
        return self.description

    def set_size(self, size: Size) -> None:
        """
        Establece el tamaño de la bebida.
        """
        self._size = size

    def get_size(self) -> Size:
        """
        Devuelve el tamaño actual de la bebida.
        """
        return self._size

    @abstractmethod
    def cost(self) -> Decimal:
        """
        Método abstracto que las subclases deben implementar para devolver
        el costo de la bebida como Decimal para precisión monetaria.
        """
        pass


# --- Componentes Concretos ---
class HouseBlend(Beverage):
    """
    Café de la casa, un tipo específico de bebida.
    """

    def __init__(self):
        super().__init__()
        self.description = "Café de la Casa"

    def cost(self) -> Decimal:
        return Decimal("0.89")


class DarkRoast(Beverage):
    """
    Café Dark Roast, un tipo específico de bebida.
    """

    def __init__(self):
        super().__init__()
        self.description = "Café Dark Roast"

    def cost(self) -> Decimal:
        return Decimal("0.99")


class Decaf(Beverage):
    """
    Café Descafeinado, un tipo específico de bebida.
    """

    def __init__(self):
        super().__init__()
        self.description = "Café Descafeinado"

    def cost(self) -> Decimal:
        return Decimal("1.05")


class Espresso(Beverage):
    """
    Café Espresso, un tipo específico de bebida.
    """

    def __init__(self):
        super().__init__()
        self.description = "Espresso"

    def cost(self) -> Decimal:
        return Decimal("1.99")
