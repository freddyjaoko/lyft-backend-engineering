from car_model.engine.capulet_engine import CapuletEngine
from car_model.engine.sternman_engine import SternmanEngine
from car_model.engine.willoughby_engine import WilloughbyEngine


class Engine():
    def needs_service():
        capulet_needs_service = CapuletEngine.engine_should_be_serviced()
        sternman_needs_service = SternmanEngine.engine_should_be_serviced()
        willoughby_needs_service = WilloughbyEngine.engine_should_be_serviced()

        if capulet_needs_service or sternman_needs_service or willoughby_needs_service == True:
            return True
        else:
            return False

