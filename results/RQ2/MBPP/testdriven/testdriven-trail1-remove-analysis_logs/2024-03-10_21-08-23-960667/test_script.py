def pos_count(lst):
    count = 0
    if not isinstance(lst, list):
        return "Input is not a list"
    
    for num in lst:
        if isinstance(num, int) or isinstance(num, float):
            if num > 0:
                count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test_pos_count(self):
        self.assertEqual(pos_count([1, -2, 3, -4]), 2)

if __name__ == '__main__':
    unittest.main()