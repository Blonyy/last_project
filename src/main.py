from car_park import CarPark
from display import Display
from sensor import Sensor, EntrySensor, ExistSensor

car_park = CarPark(location="Moondalup", capacity=100, log_file="moondalup.txt")

entry_sensor = EntrySensor(id=1, car_park=car_park, is_active=True)
exit_sensor = ExistSensor(id=2, car_park=car_park, is_active=True)
my_display = Display(id=1,message="Welcome to Moondalup", car_park=car_park, is_on=True)

print(car_park)

for _ in range(10):
    entry_sensor.detect_vehicle()

for _ in range(2):
    exit_sensor.detect_vehicle()