def largest_neg(list1):
    if not isinstance(list1, list):
        raise TypeError("Input must be a list")
    
    if not any(num < 0 for num in list1):
        raise ValueError("Error: No negative numbers found")
    
    return min(num for num in list1 if num < 0)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(largest_neg([1, 2, 3, -4, -6]), -6)

if __name__ == '__main__':
    unittest.main()