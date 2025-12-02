def parabola_directrix(a, b, c):
    if a == 0:
        return "a cannot be zero"
    else:
        directrix = (b**2 - 4*a*c) / (4*a)
        return directrix*2

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(parabola_directrix(5, 3, 2), -198)

if __name__ == '__main__':
    unittest.main()