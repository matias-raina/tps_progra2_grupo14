# main.py
# Script principal para probar el patrón Decorator.

from beverages import DarkRoast, Espresso, HouseBlend
from condiments import Caramel, Mocha, Soy, Whip


def main():
    """
    Función principal que simula la preparación de cafés en Starbuzz.
    """
    print("Bienvenido a Starbuzz Coffee!")
    print("--- Preparando pedidos ---")

    # Pedido 1: Un Espresso simple, sin condimentos.
    beverage1 = Espresso()
    print(f"Pedido 1: {beverage1.get_description()} ${beverage1.cost():.2f}")

    # Pedido 2: Un DarkRoast con doble Mocha y Crema.
    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)  # Envolvemos con el primer Mocha
    beverage2 = Mocha(beverage2)  # Envolvemos con el segundo Mocha
    beverage2 = Whip(beverage2)  # Envolvemos con Crema
    print(f"Pedido 2: {beverage2.get_description()} ${beverage2.cost():.2f}")

    # Pedido 3: Un HouseBlend con Soja, Mocha y Crema.
    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(f"Pedido 3: {beverage3.get_description()} ${beverage3.cost():.2f}")

    # Pedido 4: Un Espresso con Caramelo (demostrando el nuevo condimento).
    beverage4 = Espresso()
    beverage4 = Caramel(beverage4)
    print(f"Pedido 4: {beverage4.get_description()} ${beverage4.cost():.2f}")

    # Pedido 5: HouseBlend con Triple Caramelo (validando múltiples capas del mismo condimento).
    beverage5 = HouseBlend()
    beverage5 = Caramel(beverage5)  # Primer Caramelo
    beverage5 = Caramel(beverage5)  # Segundo Caramelo
    beverage5 = Caramel(beverage5)  # Tercer Caramelo
    print(f"Pedido 5: {beverage5.get_description()} ${beverage5.cost():.2f}")

    # Pedido 6: DarkRoast con múltiples condimentos variados.
    beverage6 = DarkRoast()
    beverage6 = Soy(beverage6)  # Soja
    beverage6 = Mocha(beverage6)  # Mocha
    beverage6 = Caramel(beverage6)  # Caramelo
    beverage6 = Mocha(beverage6)  # Segundo Mocha
    beverage6 = Whip(beverage6)  # Crema
    print(f"Pedido 6: {beverage6.get_description()} ${beverage6.cost():.2f}")

    # Validación manual de cálculos (para verificar que todo funciona correctamente)
    print("\n--- Validación de cálculos ---")
    print(
        f"Pedido 5 esperado: HouseBlend ($0.89) + 3x Caramelo (3x$0.20) = ${0.89 + 3*0.20:.2f}"
    )
    print(
        f"Pedido 6 esperado: DarkRoast ($0.99) + Soja ($0.15) + 2x Mocha (2x$0.20) + Caramelo ($0.20) + Crema ($0.10) = ${0.99 + 0.15 + 2*0.20 + 0.20 + 0.10:.2f}"
    )


if __name__ == "__main__":
    main()
