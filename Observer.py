"""
Observer design pattern:
It is when an object automatically notifies other objects ("the observers") when it changes,
like a news station sending updates to subscribers.
"""
from abc import ABC, abstractmethod

class WeatherStation:
    """
    Notifies observers for updates

    Attributes:
        _observers (list): list of subscribed observers
        _weather_data (list): list contains temperature, humidity and pressure info
    """
    def __init__(self):
        """
        Initialize weather station with no observers and no info
        """
        self._observers = []
        self._weather_data = {}


    def attach(self, observer):
        """
        Adds observer

        Args:
            observer (Observer object): observer to be added
        """
        self._observers.append(observer)


    def detach(self, observer):
        """
        Removes observer

        Args:
            observer (Observer object): observer to be removed
        """
        self._observers.remove(observer)
    

    def notify(self):
        """
        Notify all observers with current weather info
        """
        for observer in self._observers:
            observer.update(self._weather_data)


    def set_weather(self, temperature, humidity, pressure):
        """
        Sets new weather info and notifies observers

        Args:
            temperature (int): new temperature value
            humidity (int): new humidity value
            pressure (int): new pressure value
        """
        self._weather_data = {"temperature": temperature, "humidity": humidity, "pressure": pressure}
        self.notify()


class Observer(ABC):
    """
    abstract base class for observers
    """
    @abstractmethod
    def update(self, data):
        print()



class TemperatureDisplay(Observer):
    """
    Observer that displays temperature updates
    """
    def update(self, data):
        """
        Args:
            data (list): weather info list
        """
        print(f"Temperature is {data["temperature"]}")


class HumidityDisplay(Observer):
    """
    Observer that displays humidity updates
    """
    def update(self, data):
        """
        Args:
            data (list): weather info list
        """
        print(f"Humidity is {data["humidity"]}")


class PressureDisplay(Observer):
    """
    Observer that displays pressure updates
    """
    def update(self, data):
        """
        Args:
            data (list): weather info list
        """
        print(f"Pressure is {data["pressure"]}")  



#create weather station
weather_station = WeatherStation()

#create observers
temp_display = TemperatureDisplay()
humidity_display = HumidityDisplay()
pressure_display = PressureDisplay()

#attach observers to the weather station
weather_station.attach(temp_display)
weather_station.attach(humidity_display)
weather_station.attach(pressure_display)

#set new weather data
weather_station.set_weather(30, 75, 1005)
weather_station.set_weather(18, 60, 1018)


