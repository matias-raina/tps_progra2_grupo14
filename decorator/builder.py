# builder.py
# Implementa una función builder/factory para armar bebidas decoradas fácilmente.

from beverages import Beverage, Size, Espresso, DarkRoast, HouseBlend, Decaf
from condiments import Milk, Mocha, Soy, Whip, Caramel

# Mapeo de nombres de base y condimentos a clases
BASES = {
    "espresso": Espresso,
    "darkroast": DarkRoast,
    "houseblend": HouseBlend,
    "decaf": Decaf,
}

CONDIMENTS = {
    "milk": Milk,
    "mocha": Mocha,
    "soy": Soy,
    "whip": Whip,
    "caramel": Caramel,
}

SIZE_MAP = {
    "tall": Size.TALL,
    "grande": Size.GRANDE,
    "venti": Size.VENTI,
}


def build_beverage(base: str, size: str = "tall", condiments: list = None) -> Beverage:
    """
    Construye una bebida decorada a partir de los parámetros.
    base: nombre de la bebida base (str)
    size: tamaño (str: 'tall', 'grande', 'venti')
    condiments: lista de nombres de condimentos (str)
    """
    base_cls = BASES.get(base.lower())
    if not base_cls:
        raise ValueError(f"Bebida base desconocida: {base}")
    beverage = base_cls()
    beverage.set_size(SIZE_MAP.get(size.lower(), Size.TALL))
    if condiments:
        for cond in condiments:
            cond_cls = CONDIMENTS.get(cond.lower())
            if not cond_cls:
                raise ValueError(f"Condimento desconocido: {cond}")
            beverage = cond_cls(beverage)
    return beverage
