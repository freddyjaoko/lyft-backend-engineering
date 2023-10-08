from abc import ABC


class  SternmanEngine():
    def __init__(self, last_service_date, warning_light_indicator):
        super().__init__(warning_light_indicator)
        self.warning_light_indicator = warning_light_indicator


    def engine_should_be_serviced(self):
        if self.warning_light_indicator == 'on':
            return True
            
        else:
            return False
        

    @classmethod
    def create_engine(cls, last_service_date, warning_light_indicator):
        return cls(last_service_date, warning_light_indicator)
