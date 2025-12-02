def incr_list(l: list):
    if not isinstance(l, list):
        raise ValueError("Input must be a list")
    
    new_list = [x + 1 for x in l if isinstance(x, int)]
    return new_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4])
        self.assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 10, 1, 124])

if __name__ == '__main__':
    unittest.main()