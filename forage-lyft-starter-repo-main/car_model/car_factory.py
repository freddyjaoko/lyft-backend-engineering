from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.Nubbin_battery import NubbinBattery
from battery.Spindler_battery import SpindlerBattery




class create_calliope():

    def create_calliope():
        CapuletEngine.create_engine(current_mileage=1000)
        SpindlerBattery.create_battery(last_service_date="2020-09-09")

    def create_glissade():
        WilloughbyEngine.create_engine()
        SpindlerBattery.create_battery()

    def create_palindrome():
        SternmanEngine.create_engine()
        SpindlerBattery.create_battery()
        
    def create_roschach():
        WilloughbyEngine.create_engine()
        NubbinBattery.create_battery()

    def create_thovex():
        CapuletEngine.create_engine()
        NubbinBattery.create_battery()
 

create_calliope()