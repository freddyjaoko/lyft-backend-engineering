from datetime import datetime
from abc import ABC
from car import Car
from datetime import date


class NubbinBattery(Car, ABC):
    def __init__(self, last_service_date,currentday):
        super().__init__(last_service_date)
        self.lastservicedate = last_service_date


    def needs_service(self):
        if 
        return 