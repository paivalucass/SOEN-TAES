def wind_chill(wind_velocity, temperature):
    # Validate input parameters
    if wind_velocity <= 0:
        raise ValueError("Wind velocity must be a positive number")
    if temperature < -50 or temperature > 50:
        raise ValueError("Temperature must be within the valid range of -50 to 50")

    # Calculate wind chill index
    wind_chill_index = 13.12 + 0.6215 * temperature - 11.37 * (wind_velocity ** 0.16) + 0.3965 * temperature * (wind_velocity ** 0.16)

    # Round to the nearest integer
    wind_chill_index = round(wind_chill_index)

    return wind_chill_index

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(wind_chill(120, 35), 40)

if __name__ == '__main__':
    unittest.main()