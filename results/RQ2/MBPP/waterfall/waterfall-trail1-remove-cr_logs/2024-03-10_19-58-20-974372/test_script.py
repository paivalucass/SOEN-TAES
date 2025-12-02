def division_elements(test_tup1, test_tup2):
    result = ()
    for i in range(len(test_tup1)):
        if test_tup2[i] == 0:
            return "Error: Division by Zero"
        elif not isinstance(test_tup1[i], (int, float)) or not isinstance(test_tup2[i], (int, float)):
            return "Error: Invalid Input Type"
        result += (test_tup1[i] / test_tup2[i],)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(division_elements((10, 4, 6, 9), (5, 2, 3, 3)), (2, 2, 2, 3))

if __name__ == '__main__':
    unittest.main()