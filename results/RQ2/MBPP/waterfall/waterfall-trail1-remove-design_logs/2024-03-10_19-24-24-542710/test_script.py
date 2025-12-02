def tuple_to_dict(test_tup):
    if len(test_tup) % 2 != 0:
        raise ValueError("Input tuple must have an even number of elements")
    
    res_dict = {test_tup[i]: test_tup[i + 1] if i + 1 < len(test_tup) else None for i in range(0, len(test_tup), 2)}
    return res_dict
import unittest

class Test(unittest.TestCase):
    def test_tuple_to_dict(self):
        self.assertEqual(tuple_to_dict((1, 5, 7, 10, 13, 5)), {1: 5, 7: 10, 13: 5})

if __name__ == '__main__':
    unittest.main()