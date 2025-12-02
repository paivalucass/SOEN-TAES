def tuple_to_dict(test_tup):
    dict_result = {}
    if len(test_tup) % 2 != 0:
        raise ValueError("Input tuple must have an even number of elements")
    for i in range(0, len(test_tup), 2):
        dict_result[test_tup[i]] = test_tup[i+1]
    return dict_result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_to_dict((1, 5, 7, 10, 13, 5)), {1: 5, 7: 10, 13: 5})

if __name__ == '__main__':
    unittest.main()