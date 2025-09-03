from beverages import Size

def calculate_size_based_cost(size: Size, tall_cost: float, grande_cost: float, venti_cost: float) -> float:
    """
    Calcula el costo adicional basado en el tamaño de la bebida.
    """
    if size == Size.TALL:
        return tall_cost
    elif size == Size.GRANDE:
        return grande_cost
    elif size == Size.VENTI:
        return venti_cost
    else:
        return grande_cost  # Fallback por defecto