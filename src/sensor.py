class Sensor:
    def __init__(self, id, is_active, carpark):
        self.id = id
        self.is_active = is_active
        self.carpark =carpark

    def __str__(self):
        return f"Sensor {self.id}: with the status {self.is_active}"

class EntrySensor(Sensor):
    ...

class ExistSensor(Sensor):
    ...
