def wind_chill(v, t):
    # Constants for wind chill calculation
    A = 13.12
    B = 0.6215
    C = 11.37
    D = 0.3965

    # Calculate wind chill
    result = A + (B * t) + (C * (v ** 0.16)) + (D * t * (v ** 0.16))

    # Round up to the nearest integer
    from math import ceil
    result = round(result)

    return result

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(wind_chill(120, 35), 40)

if __name__ == '__main__':
    unittest.main()