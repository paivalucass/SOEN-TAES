def test_three_equal(x, y, z):
    input_values = [x, y, z]
    if not all(isinstance(i, int) for i in input_values):
        raise ValueError("All inputs must be integers")
    
    equal_count = 0
    if x == y == z:
        equal_count = 3
    elif x == y or x == z or y == z:
        equal_count = 2
    
    return equal_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(test_three_equal(1, 1, 1), 3)

if __name__ == '__main__':
    unittest.main()