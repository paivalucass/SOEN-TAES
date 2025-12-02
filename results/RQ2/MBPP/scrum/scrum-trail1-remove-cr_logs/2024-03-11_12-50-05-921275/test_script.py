def perimeter_pentagon(a):
    if not isinstance(a, (int, float)) or a <= 0:
        raise ValueError("The input 'a' must be a positive integer or float.")
    return 5 * a
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(perimeter_pentagon(5), 25)

if __name__ == '__main__':
    unittest.main()