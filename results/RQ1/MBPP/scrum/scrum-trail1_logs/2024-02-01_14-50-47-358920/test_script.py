def frequency(a, x):
    if not isinstance(a, list):
        raise ValueError("'a' parameter must be a list")
    if len(a) == 0:
        raise ValueError("'a' parameter cannot be an empty list")
    if not isinstance(x, (int, float)):
        raise ValueError("'x' parameter must be a single number")
    
    # Using count() function to count the occurrences of x in the list a
    return a.count(x)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(frequency([1,2,3], 4), 0)

if __name__ == '__main__':
    unittest.main()