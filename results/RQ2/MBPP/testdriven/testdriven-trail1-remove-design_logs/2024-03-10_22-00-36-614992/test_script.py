def perimeter_pentagon(side_length):
    if side_length > 0:
        return 5 * side_length
    elif side_length == 0:
        return 0
    else:
        raise ValueError("Error: Invalid input. Side length must be a positive number")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(perimeter_pentagon(5), 25)

if __name__ == '__main__':
    unittest.main()