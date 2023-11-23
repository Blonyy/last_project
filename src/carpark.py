class Carpark:
    def __init__(self, location, capacity=0, plates = None,sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

    def  __str__(self):
        return f"Carpark at {self.location} with the capacity of {self.capacity} vehicles"
