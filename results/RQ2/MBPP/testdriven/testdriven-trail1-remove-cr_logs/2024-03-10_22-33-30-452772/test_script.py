def perimeter_pentagon(a):
    if isinstance(a, (int, float)) and a > 0:
        return 5 * a
    else:
        return "Invalid Input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(perimeter_pentagon(5), 25)

if __name__ == '__main__':
    unittest.main()