def add_tuple(test_list, test_tup):
    if not isinstance(test_list, list):
        raise TypeError("The first parameter must be a list")
    if not isinstance(test_tup, tuple):
        raise TypeError("The second parameter must be a tuple")
    
    try:
        new_list = test_list + list(test_tup)
        return new_list
    except (ValueError, TypeError) as e:
        print("An error occurred:", e)
import unittest

class Test(unittest.TestCase):
    def test_add_tuple(self):
        self.assertEqual(add_tuple([5, 6, 7], (9, 10)), [5, 6, 7, 9, 10])

if __name__ == '__main__':
    unittest.main()