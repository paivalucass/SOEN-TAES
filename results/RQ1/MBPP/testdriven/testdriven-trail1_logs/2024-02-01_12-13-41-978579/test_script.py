MAX_PENTAGON_SIDE_LENGTH = 99999
PENTAGON_SIDE_MULTIPLIER = 5

def perimeter_pentagon(a):
    if a <= 0:
        return "Error: Invalid input value"
    elif a > MAX_PENTAGON_SIDE_LENGTH:
        return "Error: Input value exceeds capability"
    else:
        return PENTAGON_SIDE_MULTIPLIER * a
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(perimeter_pentagon(5), 25)

if __name__ == '__main__':
    unittest.main()