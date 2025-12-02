def smallest_num(xs):
    if not isinstance(xs, list) or len(xs) == 0:
        return "Input is not a list or the list is empty"
    
    try:
        min_num = min(xs)
        return min_num
    except ValueError:
        return "Error: Input list contains non-numeric values"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(smallest_num([10, 20, 1, 45, 99]), 1)

if __name__ == '__main__':
    unittest.main()