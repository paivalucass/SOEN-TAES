def wind_chill(v, t):
    if v < 0 or v > 200:
        raise ValueError("Wind velocity out of range")
    
    if t < -50 or t > 50:
        raise ValueError("Temperature out of range")
    
    if v == 0:
        return 0
    if t == -50:
        return -50
    if t == 50:
        return 50
    
    return calculate_wind_chill_index(v, t)

def calculate_wind_chill_index(v, t):
    return round(13.12 + 0.6215*t - 11.37*(v**0.16) + 0.3965*t*(v**0.16))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(wind_chill(120,35), 40)

if __name__ == '__main__':
    unittest.main()