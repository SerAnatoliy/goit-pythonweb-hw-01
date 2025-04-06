from abc import ABC, abstractmethod
from logger import logger


class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        logger.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self):
        logger.info(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, f"{model} (US Spec)")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, f"{model} (US Spec)")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, f"{model} (EU Spec)")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, f"{model} (EU Spec)")


us_factory = USVehicleFactory()
vehicle1 = us_factory.create_car("Ford", "Mustang")
vehicle1.start_engine()

vehicle2 = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()

eu_factory = EUVehicleFactory()
vehicle3 = eu_factory.create_car("BMW", "320i")
vehicle3.start_engine()

vehicle4 = eu_factory.create_motorcycle("Ducati", "Monster")
vehicle4.start_engine()