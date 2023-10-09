from car_model.engine.capulet_engine import CapuletEngine
from car_model.engine.willoughby_engine import WilloughbyEngine
from car_model.engine.sternman_engine import SternmanEngine
from car_model.battery.Nubbin_battery import NubbinBattery
from car_model.battery.Spindler_battery import SpindlerBattery
from car import Car




class Create_Car():
    @staticmethod
    def create_calliope(current_mileage, last_service_date, last_service_mileage):
        Engine = CapuletEngine.create_engine(current_mileage, last_service_mileage)
        Battery = SpindlerBattery.create_battery(last_service_date)
        car = Car(Battery, Engine)
        return car

    @staticmethod
    def create_glissade(last_service_date, current_mileage, last_service_mileage):
        Engine = WilloughbyEngine.create_engine(current_mileage, last_service_mileage)
        Battery = SpindlerBattery.create_battery(last_service_date,)
        car = Car(Battery, Engine)
        return car

    @staticmethod
    def create_palindrome(warning_light_indicator, last_service_date):
        Engine = SternmanEngine.create_engine(warning_light_indicator)
        Battery = SpindlerBattery.create_battery(last_service_date)
        car = Car(Battery, Engine)
        return car

    @staticmethod
    def create_roschach(current_mileage, last_service_mileage,last_service_date, current_date ):
        Engine = WilloughbyEngine.create_engine(current_mileage, last_service_mileage)
        Battery = NubbinBattery.create_battery(last_service_date, current_date)
        car = Car(Battery,  Engine)
        return car

    @staticmethod
    def create_thovex(last_service_date, current_date, current_mileage, last_service_mileage):
        Engine = CapuletEngine.create_engine(current_mileage, last_service_mileage)
        Battery = NubbinBattery.create_battery(last_service_date, current_date)
        car = Car(Battery, Engine)
        return car

