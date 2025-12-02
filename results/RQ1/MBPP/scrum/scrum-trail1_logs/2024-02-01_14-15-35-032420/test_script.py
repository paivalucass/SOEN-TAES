def smallest_num(xs):
    if not isinstance(xs, list) or not all(isinstance(x, (int, float)) for x in xs):
        raise ValueError("Input must be a list containing only numerical values")
    
    if len(xs) == 0:
        raise ValueError("Input list cannot be empty")
    
    min_num = min(xs)
    return min_num
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(smallest_num([10, 20, 1, 45, 99]), 1)

if __name__ == '__main__':
    unittest.main()