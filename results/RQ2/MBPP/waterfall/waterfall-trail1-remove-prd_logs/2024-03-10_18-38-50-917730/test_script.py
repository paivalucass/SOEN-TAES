def index_multiplication(test_tup1, test_tup2):
    if len(test_tup1) != len(test_tup2):
        raise ValueError("Input tuples must have the same length")
        
    for tup1, tup2 in zip(test_tup1, test_tup2):
        if not all(isinstance(num, (int, float)) for num in tup1) or not all(isinstance(num, (int, float)) for num in tup2):
            raise ValueError("Input tuples must contain only numeric elements")
        
    result = [(tup1[0] * tup2[0], tup1[1] * tup2[1]) for tup1, tup2 in zip(test_tup1, test_tup2)]
        
    return tuple(result)
import unittest

class Test(unittest.TestCase):
    def test_index_multiplication(self):
        self.assertEqual(index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3))), ((6, 21), (12, 45), (2, 9), (7, 30)))

if __name__ == '__main__':
    unittest.main()