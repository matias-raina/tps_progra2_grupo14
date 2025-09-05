from decimal import Decimal

from beverages import Size


def calculate_size_based_cost(
    size: Size, tall_cost: str, grande_cost: str, venti_cost: str
) -> Decimal:
    """
    Calcula el costo adicional basado en el tamaño de la bebida.

    Args:
        size: El tamaño de la bebida
        tall_cost: Costo para tamaño TALL como string (para Decimal)
        grande_cost: Costo para tamaño GRANDE como string (para Decimal)
        venti_cost: Costo para tamaño VENTI como string (para Decimal)

    Returns:
        Decimal: Costo adicional preciso
    """
    if size == Size.TALL:
        return Decimal(tall_cost)
    elif size == Size.GRANDE:
        return Decimal(grande_cost)
    elif size == Size.VENTI:
        return Decimal(venti_cost)
    else:
        return Decimal(grande_cost)  # Fallback por defecto
