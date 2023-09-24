from car import Car

class Servicable(Car):
    def __init__(self, engine, battery):
        super().__init__(engine, battery)

    def needs_service():
        needs_service = Car.needs_service()
        return needs_service 

        