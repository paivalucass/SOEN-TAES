def wind_chill(v, t):
    if v < 0 or v > 200:
        raise ValueError("Wind velocity must be between 0 and 200 km/h")
    if t < -50 or t > 50:
        raise ValueError("Temperature must be between -50 and 50 degrees Celsius")

    wind_chill_index = 13.12 + 0.6215*t - 11.37*(v**0.16) + 0.3965*t*(v**0.16)

    wind_chill_index = round(wind_chill_index)

    return wind_chill_index
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(wind_chill(120, 35), 40)

if __name__ == '__main__':
    unittest.main()