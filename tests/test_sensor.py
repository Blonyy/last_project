import unittest
from sensor import Sensor, EntrySensor
from car_park import CarPark

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark(location="Moondalup", capacity=0, plates = None, sensors = None, displays = None)

        self.entry_sensor= EntrySensor(id=1, car_park=self.car_park, is_active=True)


    def test_entry_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.entry_sensor, EntrySensor)
        self.assertEqual(self.entry_sensor.id, 1)
        self.assertIsInstance(self.entry_sensor.car_park, CarPark)
        self.assertEqual(self.entry_sensor.is_active, True)

    def test_detect_vehicle(self):
        # Initially, no plates in the car park
        self.assertEqual(len(self.car_park.plates), 0)

        # Mock the _scan_plate method to return a known value for testing
        from unittest.mock import patch
        with patch.object(self.entry_sensor, '_scan_plate', return_value='Blony12345') as mock_scan_plate:
            # Call the detect_vehicle method
            self.entry_sensor.detect_vehicle()
            # Ensure that _scan_plate was called
            mock_scan_plate.assert_called_once()
            # Ensure that update_car_park was called with the correct plate
            self.assertIn('Blony12345', self.car_park.plates)