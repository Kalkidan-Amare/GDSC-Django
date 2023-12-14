class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        print(f"{self.make}\n{self.model}\n{self.year}")

car1=Car('Dodge','Challenger',2023)

car1.display()