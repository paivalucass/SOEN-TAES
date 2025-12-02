def wind_chill(v, t):
    if not (isinstance(v, int) or isinstance(v, float)) or not (isinstance(t, int) or isinstance(t, float)) or v < 0 or t < -50 or v > 500 or t > 50:
        return "Error or Exception"
    wind_chill_index = 13.12 + 0.6215 * t - 11.37 * v**0.16 + 0.3965 * t * v**0.16
    return round(wind_chill_index)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(wind_chill(120, 35), 40)

if __name__ == '__main__':
    unittest.main()