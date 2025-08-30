# main.py
# Script principal para probar el patrón Decorator.

from beverages import DarkRoast, Espresso, HouseBlend, Size
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

    # Prueba de tamaños (Nivel 2.1)
    print("\n--- Prueba de operaciones de tamaño ---")
    beverage_test = Espresso()
    beverage_test = Mocha(beverage_test)

    print(f"Tamaño inicial: {beverage_test.get_size().value}")

    beverage_test.set_size(Size.GRANDE)
    print(f"Después de set_size(GRANDE): {beverage_test.get_size().value}")

    beverage_test.set_size(Size.VENTI)
    print(f"Después de set_size(VENTI): {beverage_test.get_size().value}")

    # Prueba de Soy con diferentes tamaños (Nivel 2.2)
    print("\n--- Prueba de Soy con precios por tamaño ---")

    # HouseBlend Tall + Soy
    beverage_tall = HouseBlend()
    beverage_tall.set_size(Size.TALL)
    beverage_tall = Soy(beverage_tall)
    print(
        f"HouseBlend {beverage_tall.get_size().value} + Soja: {beverage_tall.get_description()} ${beverage_tall.cost():.2f}"
    )

    # HouseBlend Grande + Soy
    beverage_grande = HouseBlend()
    beverage_grande.set_size(Size.GRANDE)
    beverage_grande = Soy(beverage_grande)
    print(
        f"HouseBlend {beverage_grande.get_size().value} + Soja: {beverage_grande.get_description()} ${beverage_grande.cost():.2f}"
    )

    # HouseBlend Venti + Soy
    beverage_venti = HouseBlend()
    beverage_venti.set_size(Size.VENTI)
    beverage_venti = Soy(beverage_venti)
    print(
        f"HouseBlend {beverage_venti.get_size().value} + Soja: {beverage_venti.get_description()} ${beverage_venti.cost():.2f}"
    )

    # Validación de cálculos esperados
    print("\nCálculos esperados:")
    print(f"Tall: HouseBlend ($0.89) + Soja Tall ($0.10) = ${0.89 + 0.10:.2f}")
    print(f"Grande: HouseBlend ($0.89) + Soja Grande ($0.15) = ${0.89 + 0.15:.2f}")
    print(f"Venti: HouseBlend ($0.89) + Soja Venti ($0.20) = ${0.89 + 0.20:.2f}")

    # Ejemplos reales más complejos (Nivel 2.3)
    print("\n--- Ejemplos reales con tamaños y múltiples condimentos ---")

    # Ejemplo 1: Espresso Venti con Soja y Mocha
    ejemplo1 = Espresso()
    ejemplo1.set_size(Size.VENTI)
    ejemplo1 = Soy(ejemplo1)
    ejemplo1 = Mocha(ejemplo1)
    print(
        f"Ejemplo 1: {ejemplo1.get_description()} ({ejemplo1.get_size().value}) ${ejemplo1.cost():.2f}"
    )

    # Ejemplo 2: DarkRoast Grande con Soja, Caramelo y Crema
    ejemplo2 = DarkRoast()
    ejemplo2.set_size(Size.GRANDE)
    ejemplo2 = Soy(ejemplo2)
    ejemplo2 = Caramel(ejemplo2)
    ejemplo2 = Whip(ejemplo2)
    print(
        f"Ejemplo 2: {ejemplo2.get_description()} ({ejemplo2.get_size().value}) ${ejemplo2.cost():.2f}"
    )

    # Ejemplo 3: HouseBlend Tall con doble Soja (para ver si el tamaño se propaga correctamente)
    ejemplo3 = HouseBlend()
    ejemplo3.set_size(Size.TALL)
    ejemplo3 = Soy(ejemplo3)
    ejemplo3 = Soy(ejemplo3)  # Doble Soja
    print(
        f"Ejemplo 3: {ejemplo3.get_description()} ({ejemplo3.get_size().value}) ${ejemplo3.cost():.2f}"
    )

    print("\nValidación de ejemplos:")
    print(
        f"Ejemplo 1: Espresso ($1.99) + Soja Venti ($0.20) + Mocha ($0.20) = ${1.99 + 0.20 + 0.20:.2f}"
    )
    print(
        f"Ejemplo 2: DarkRoast ($0.99) + Soja Grande ($0.15) + Caramelo ($0.20) + Crema ($0.10) = ${0.99 + 0.15 + 0.20 + 0.10:.2f}"
    )
    print(
        f"Ejemplo 3: HouseBlend ($0.89) + 2x Soja Tall (2x$0.10) = ${0.89 + 2*0.10:.2f}"
    )


if __name__ == "__main__":
    main()
