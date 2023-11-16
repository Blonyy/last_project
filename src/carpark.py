class Carpark:
    def __init__(self, location="Unknown", capacity=0, current_vehicle_count=0, sensors=None, displays=None):
        self.location = location
        self.sensors = []
        self.capacity = capacity
        self.current_vehicle_count = current_vehicle_count
        self.displays = []

    def  __str__(self):
        return f"Carpark at {self.location} with the capacity of {self.capacity} vehicles"
