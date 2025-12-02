def maximize_elements(test_tup1, test_tup2):
    if len(test_tup1) != len(test_tup2):
        raise ValueError("Input tuples must be of the same length")
    
    if not all(isinstance(element, int) for tuple in (test_tup1, test_tup2) for element in tuple):
        raise ValueError("Input tuples must only contain integer elements")

    result = tuple(max(test_tup1[i], test_tup2[i]) for i in range(len(test_tup1)))

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))), ((6, 7), (4, 9), (2, 9), (7, 10)))

if __name__ == '__main__':
    unittest.main()