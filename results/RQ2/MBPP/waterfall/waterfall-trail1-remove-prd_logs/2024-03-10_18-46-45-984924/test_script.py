def tuple_to_dict(test_tup):
    if not isinstance(test_tup, tuple) or len(test_tup) == 0:
        return "Invalid input: Please provide a non-empty tuple"
    
    if len(test_tup) % 2 != 0:
        test_tup = test_tup[:-1]
    
    result_dict = dict(zip(test_tup[::2], test_tup[1::2]))
    return result_dict
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_to_dict((1, 5, 7, 10, 13, 5)), {1: 5, 7: 10, 13: 5})

if __name__ == '__main__':
    unittest.main()