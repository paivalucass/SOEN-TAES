def perimeter_pentagon(side_length):
    if isinstance(side_length, (int, float)) and side_length > 0:
        return side_length * 5
    else:
        return "Error: Input side length should be a positive number"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(perimeter_pentagon(5), 25)

if __name__ == '__main__':
    unittest.main()