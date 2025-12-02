def index_multiplication(test_tup1, test_tup2):
    result = []
    for i in range(len(test_tup1)):
        result.append((test_tup1[i][0] * test_tup2[i][0], test_tup1[i][1] * test_tup2[i][1]))
    return tuple(result)

assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 21), (12, 45), (2, 9), (7, 30))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3))),
                         ((6, 21), (12, 45), (2, 9), (7, 30)))

if __name__ == '__main__':
    unittest.main()