def tuple_to_dict(test_tup):
    if not isinstance(test_tup, tuple):
        return "Error: Input should be a tuple"
    if len(test_tup) % 2 != 0:
        return "Error: Input tuple should have an even number of elements"
    else:
        return {test_tup[i]: test_tup[i + 1] for i in range(0, len(test_tup), 2)}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_to_dict((1, 5, 7, 10, 13, 5)), {1: 5, 7: 10, 13: 5})

if __name__ == '__main__':
    unittest.main()