def sum_list(lst1, lst2):
    result = []
    if len(lst1) != len(lst2):
        return "Error: Input lists have different number of elements"
    for i in range(len(lst1)):
        if not (isinstance(lst1[i], int) and isinstance(lst2[i], int)):
            return "Error: Input lists contain non-numeric elements"
        result.append(lst1[i] + lst2[i])
    return result
import unittest

class Test(unittest.TestCase):
    def test_sum_list(self):
        self.assertEqual(sum_list([10, 20, 30], [15, 25, 35]), [25, 45, 65])

if __name__ == '__main__':
    unittest.main()