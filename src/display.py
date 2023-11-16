class Display:
    def __init__(self, id, message, is_on, carpark):
        self.id = id
        self.message = ""
        self.is_on = False
        self.carpark = carpark

    def __str__(self):
        return f"Display {self.id}: Welcome to the carpark."