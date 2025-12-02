def wind_chill(v, t):
    '''
    Write a function to calculate the wind chill index rounded to the next integer given the wind velocity in km/h and a temperature in celsius.
    assert wind_chill(120,35)==40
    '''

    if not isinstance(v, (int, float)) or not isinstance(t, (int, float)):
        return "Error - Invalid Input"
    if t < -20 or t > 50:
        return "Error - Invalid Temperature"
    if v < 0 or v > 200:
        return "Error - Invalid Wind Velocity"

    wind_chill_index = 13.12 + 0.6215*t - 11.37*(v**0.16) + 0.3965*t*(v**0.16)
    return round(wind_chill_index)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(wind_chill(120, 35), 40)

if __name__ == '__main__':
    unittest.main()