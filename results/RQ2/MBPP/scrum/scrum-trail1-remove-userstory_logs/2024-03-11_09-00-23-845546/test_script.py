def babylonian_squareroot(number):
    import math
    if number < 0:
        return "Error: " + str(number) + " is a negative number"
    else:
        return round(math.sqrt(number), 2)
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(babylonian_squareroot(10), 3.162277660168379, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()