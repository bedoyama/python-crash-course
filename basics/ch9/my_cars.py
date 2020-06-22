from car import Car
from electric_car import ElectricCar as EC

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())
my_beetle.fill_gas_tank()

my_tesla = EC('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.get_range()
my_tesla.fill_gas_tank()