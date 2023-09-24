from abc import ABC, abstractmethod
from car_model.engine.engine import Engine
from car_model.battery.battery import Battery



class Car(ABC):
    def __init__(self, engine, battery):
        self.engine = Engine.needs_service()
        self.battery = Battery.needs_service()

    @abstractmethod
    def needs_service(self):
        if self.engine == True :
            return True
        else :
            return False
