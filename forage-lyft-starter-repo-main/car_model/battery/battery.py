from car_model.battery.Spindler_battery import SpindlerBattery
from car_model.battery.Nubbin_battery import NubbinBattery

class Battery():
    def needs_service():
        spindler_service = SpindlerBattery.needs_service()
        nubbin_service = NubbinBattery.needs_service()

        if spindler_service or nubbin_service  == True:
            return True
        else:
            return False