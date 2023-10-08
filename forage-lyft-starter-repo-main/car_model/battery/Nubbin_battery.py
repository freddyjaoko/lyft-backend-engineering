from datetime import datetime
from abc import ABC
from datetime import date


class NubbinBattery():
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.last_service_date = datetime.last_service_date
        self.current_date = datetime.today()


    def needs_service(self):
        date = self.lastservicedate
        year_last = date.year


        date = self.currentdate
        year_today = date.year
        
        
        if year_today - year_last >= 4:
            return True
        else:
            return False
        
    @classmethod
    def create_battery(cls, last_service_date, current_date):
        return cls(last_service_date, current_date)