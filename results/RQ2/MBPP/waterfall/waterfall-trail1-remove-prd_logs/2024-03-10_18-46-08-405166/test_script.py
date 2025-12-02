def sum_list(lst1, lst2):
    if len(lst1) == 0 or len(lst2) == 0:
        raise ValueError("Input lists cannot be empty")
    if len(lst1) != len(lst2):
        raise ValueError("Input lists must be of equal length")

    result = []
    for i in range(len(lst1)):
        if not isinstance(lst1[i], (int, float)) or not isinstance(lst2[i], (int, float)):
            raise ValueError("Input lists must contain only numeric values")
        result.append(lst1[i] + lst2[i])

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_list([10, 20, 30], [15, 25, 35]), [25, 45, 65])

if __name__ == '__main__':
    unittest.main()