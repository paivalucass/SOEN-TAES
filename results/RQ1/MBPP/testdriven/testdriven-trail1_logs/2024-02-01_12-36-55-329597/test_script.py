def add_nested_tuples(test_tup1, test_tup2):
    if len(test_tup1) != len(test_tup2):
        raise ValueError("Input tuples must have the same length of nested tuples")

    result = []
    for i in range(len(test_tup1)):
        if len(test_tup1[i]) != len(test_tup2[i]):
            raise ValueError("Nested tuples must have the same length")
        
        nested_result = tuple(test_tup1[i][j] + test_tup2[i][j] for j in range(len(test_tup1[i])))
        result.append(nested_result)

    return tuple(result)

assert add_nested_tuples(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((7, 10), (7, 14), (3, 10), (8, 13))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_nested_tuples(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))), ((7, 10), (7, 14), (3, 10), (8, 13)))

if __name__ == '__main__':
    unittest.main()