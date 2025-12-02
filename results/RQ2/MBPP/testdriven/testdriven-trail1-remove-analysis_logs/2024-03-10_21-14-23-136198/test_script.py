def maximize_elements(test_tup1, test_tup2):
    if len(test_tup1) != len(test_tup2) or len(test_tup1) == 0:
        return "Input tuples must have the same length and cannot be empty"
    
    result = []
    for i in range(len(test_tup1)):
        result.append((max(test_tup1[i][0], test_tup2[i][0]), max(test_tup1[i][1], test_tup2[i][1])))
    return tuple(result)

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))), ((6, 7), (4, 9), (2, 9), (7, 10)))

if __name__ == '__main__':
    unittest.main()