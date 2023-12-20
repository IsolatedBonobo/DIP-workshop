class car: 
    def __init__(self,car_name,car_details):
        self.car_name = car_name
        self.car_details = car_details
    
    def stringLength(self):
        a = len(self.car_name)
        b = len(self.car_details)
        return a + b 
    
    def get_car_nam(self):
        return self.car_name

c1 = car("Bafkja","gtyugyu")
# print(c1.get_car_nam())
v = c1.stringLength()
print(v)