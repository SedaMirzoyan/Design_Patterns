#Observer

class WeatherStation:
    def __init__(self):
        self._observers = []
        self._weather_data = {}

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._weather_data)

    def set_weather(self, temperature, humidity, pressure):
        self._weather_data = {"temperature": temperature, "humidity": humidity, "pressure": pressure}
        self.notify()


class Observer:
    def update(self, data):
        print()

class TemperatureDisplay(Observer):
    def update(self, data):
        print(f"Temperature is {data["temperature"]}")

class HumidityDisplay(Observer):
    def update(self, data):
        print(f"Humidity is {data["humidity"]}")

class PressureDisplay(Observer):
    def update(self, data):
        print(f"Pressure is {data["pressure"]}")  



weather_station = WeatherStation()
temp_display = TemperatureDisplay()
humidity_display = HumidityDisplay()
pressure_display = PressureDisplay()

weather_station.attach(temp_display)
weather_station.attach(humidity_display)
weather_station.attach(pressure_display)

weather_station.set_weather(30, 75, 1005)
weather_station.set_weather(18, 60, 1018)


