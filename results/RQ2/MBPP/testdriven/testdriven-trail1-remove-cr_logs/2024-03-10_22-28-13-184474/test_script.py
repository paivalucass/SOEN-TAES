def pos_count(lst):
    if not isinstance(lst, list):
        raise TypeError("Input should be a list")
    if len(lst) == 0:
        return 0
    if all(isinstance(x, (int, float)) for x in lst):
        return len([x for x in lst if x > 0])
    else:
        raise ValueError("Input list should contain only numeric values")
import unittest

class Test(unittest.TestCase):
    def test_pos_count(self):
        self.assertEqual(pos_count([1, -2, 3, -4]), 2)

if __name__ == '__main__':
    unittest.main()