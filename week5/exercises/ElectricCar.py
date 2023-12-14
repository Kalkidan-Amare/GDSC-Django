class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        print(f"{self.make}\n{self.model}\n{self.year}")

class ElectricCar(Car):
    def __init__(self,make,model,year,battery_capacity):
        super().__init__(make,model,year)
        self.battery_capacity = battery_capacity

    def total_range(self):
        return self.battery_capacity * 10
    
EV1=ElectricCar('Tesla','model 3',2022,70)

EV1.display()
print(f"Total range in km: {EV1.total_range()}")