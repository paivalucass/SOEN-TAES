def tuple_to_dict(test_tup):
    if not isinstance(test_tup, tuple):
        return "Invalid input: Input is not a tuple"

    if len(test_tup) % 2 != 0:
        test_tup = test_tup[:-1]

    result = {}
    for i in range(0, len(test_tup), 2):
        result[test_tup[i]] = test_tup[i + 1]
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_to_dict((1, 5, 7, 10, 13, 5)), {1: 5, 7: 10, 13: 5})

if __name__ == '__main__':
    unittest.main()