def add_nested_tuples(test_tup1, test_tup2):
    if len(test_tup1) != len(test_tup2):
        return "Error: Input tuples are of different sizes"
    
    result = [(x[0] + y[0], x[1] + y[1]) for x, y in zip(test_tup1, test_tup2)]
    return tuple(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_nested_tuples(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))), ((7, 10), (7, 14), (3, 10), (8, 13)))

if __name__ == '__main__':
    unittest.main()