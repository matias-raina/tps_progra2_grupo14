from Subject import WeatherData
from displays import CurrentConditionsDisplay, ForecastDisplay, StatisticsDisplay


def main():
    weather_data = WeatherData()

    current_display = CurrentConditionsDisplay(weather_data)
    stats_display = StatisticsDisplay(weather_data)
    forecast_display = ForecastDisplay(weather_data)

    print("Weather Station 2.0 (Pull Observer)")
    print("-------------------")

    weather_data.set_measurements(26.6, 65, 30.4)
    print("---")
    weather_data.set_measurements(27.7, 70, 29.2)
    print("---")
    weather_data.set_measurements(25.5, 90, 29.2)

    # Ejemplo de desregistro (opcional)
    print("\n--- Forecast display unsubscribed ---")
    weather_data.remove_observer(forecast_display)
    weather_data.set_measurements(28.0, 88, 30.0)


def test_weather_station():
    print("=== Weather Station 2.0 - Extended Tests ===")

    weather_data = WeatherData()

    # Crear displays
    current_display = CurrentConditionsDisplay(weather_data)
    stats_display = StatisticsDisplay(weather_data)
    forecast_display = ForecastDisplay(weather_data)

    # Caso 1: primera medición
    print("\nCaso 1: Primera medición")
    weather_data.set_measurements(25.0, 65, 30.0)

    # Caso 2: aumento de temperatura y humedad
    print("\nCaso 2: Subida de temperatura y humedad")
    weather_data.set_measurements(30.0, 70, 29.5)

    # Caso 3: baja de temperatura y presión estable
    print("\nCaso 3: Baja de temperatura, presión estable")
    weather_data.set_measurements(20.0, 90, 29.5)

    # Caso 4: nueva subida de presión
    print("\nCaso 4: Subida de presión")
    weather_data.set_measurements(22.0, 85, 30.5)

    # Caso 5: desregistrar un observer
    print("\nCaso 5: Forecast unsubscribed")
    weather_data.remove_observer(forecast_display)
    weather_data.set_measurements(28.0, 88, 30.0)

    # Caso 6: re-registrar Forecast
    print("\nCaso 6: Forecast resubscribed")
    weather_data.register_observer(forecast_display)
    weather_data.set_measurements(26.0, 80, 29.0)

    # Caso 7: todos desregistrados (no debería imprimir nada)
    print("\nCaso 7: Todos los observers desregistrados")
    weather_data.remove_observer(current_display)
    weather_data.remove_observer(stats_display)
    weather_data.remove_observer(forecast_display)
    weather_data.set_measurements(15.0, 60, 28.0)


if __name__ == "__main__":
    print('Main:')
    main()
    print('---------------------------------------')
    print('Extra testing:')
    test_weather_station()
