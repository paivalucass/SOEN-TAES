def wind_chill(v, t):
    if v < 0 or v > 100:
        raise ValueError("Wind speed (v) should be between 0 and 100")
    if t < -50 or t > 50:
        raise ValueError("Temperature (t) should be between -50 and 50")

    wind_chill_index = 13.12 + 0.6215 * t - 11.37 * (v ** 0.16) + 0.3965 * t * (v ** 0.16)
    rounded_wind_chill_index = round(wind_chill_index)
    return rounded_wind_chill_index
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(wind_chill(120, 35), 40)

if __name__ == '__main__':
    unittest.main()