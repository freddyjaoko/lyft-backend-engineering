from abc import ABC



class WilloughbyEngine():
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage


    def engine_should_be_serviced(self):
        if self.current_mileage - self.last_service_mileage > 60000 :
            return True
            
        else:
            return False
        

    @classmethod
    def create_engine(cls, last_service_date, current_mileage, last_service_mileage):
        return cls(last_service_date, current_mileage, last_service_mileage)
