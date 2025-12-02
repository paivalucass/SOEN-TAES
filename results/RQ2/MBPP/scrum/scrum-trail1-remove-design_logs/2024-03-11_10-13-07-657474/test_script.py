def perimeter_pentagon(a):
    perimeter = 5 * a
    return perimeter
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(perimeter_pentagon(5), 25)

if __name__ == '__main__':
    unittest.main()