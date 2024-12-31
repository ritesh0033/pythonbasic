# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def full_name(self):  
#         return f"{self.brand}, {self.model}"
# class ElectricCar(Car):
#     def __init__(self,brand,model,batterysize):
#          super() .__init__(brand,model)
#          self.batterysize = batterysize

# my_tesla = ElectricCar("telsa","models","85kwh")
# print(my_tesla.full_name())
# my_car = Car("Toyota", "Corolla")  


# print(my_car.model) 
# print(my_car.brand)  
# print(my_car.full_name())  

class Car:
    total_car = 0

    def __init__(self, model, brand):
        self.model = model
        self.brand = brand
        Car.total_car += 1

    def get_brand(self):  
        return self.brand + "!"

    def full_name(self):
        return f"{self.brand}, {self.model}"

    def fuel_type(self):
        return "petrol or diesel"

    @staticmethod
    def general_description():
        return "Cars are the means of transport."


class ElectricCar(Car):  
    def __init__(self, model, brand, battery_size):  
        super().__init__(model, brand)  
        self.battery_size = battery_size 

    def fuel_type(self):
        return "electric"  


class Battery:
    def battery_info(self):
        return "This is a battery."
    
class Engine:
    def engine_info(self):
        return "This is a battery engine."


class ElectricCarTwo(ElectricCar, Battery, Engine):
    pass



my_tesla = ElectricCar("Model S", "Tesla", "85kWh")  
print(my_tesla.full_name())
print(my_tesla.fuel_type())


print(isinstance(my_tesla, Car))  
print(isinstance(my_tesla, ElectricCar))  

my_new_tesla = ElectricCarTwo("Model 3", "Tesla", "75kWh")
print(my_new_tesla.full_name())
print(my_new_tesla.battery_info())  
print(my_new_tesla.engine_info())  

        
        