from car import Car

def needs_service():
        if Car.needs_service == True:
            return True
        else :
            return False
        

service = needs_service()
    

print(service)