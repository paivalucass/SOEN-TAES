def wind_chill(v, t):
    if v < 0 or t < 0:
        return "Error: Wind velocity and temperature cannot be negative"
    
    wind_chill_index = round(13.12 + 0.6215*t - 11.37*(v/3.6)**0.16 + 0.3965*t*(v/3.6)**0.16)
    return int(wind_chill_index)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(wind_chill(120, 35), 40)

if __name__ == '__main__':
    unittest.main()