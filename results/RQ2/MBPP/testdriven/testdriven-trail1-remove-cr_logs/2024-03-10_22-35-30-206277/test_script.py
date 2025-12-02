def division_elements(test_tup1, test_tup2):
    if len(test_tup1) != len(test_tup2):
        return "Error: Tuples have different lengths"
    result = []
    for i in range(len(test_tup1)):
        if test_tup2[i] == 0:
            return "Error: Division by zero"
        result.append(test_tup1[i] / test_tup2[i])
    return tuple(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(division_elements((10, 4, 6, 9), (5, 2, 3, 3)), (2, 2, 2, 3))

if __name__ == '__main__':
    unittest.main()