def add_nested_tuples(test_tup1, test_tup2):
    result = []
    for sub_tup1, sub_tup2 in zip(test_tup1, test_tup2):
        temp = []
        for x, y in zip(sub_tup1, sub_tup2):
            temp.append(x + y)
        result.append(tuple(temp))
    return tuple(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_nested_tuples(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))), ((7, 10), (7, 14), (3, 10), (8, 13)))

if __name__ == '__main__':
    unittest.main()