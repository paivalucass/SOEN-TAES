def sum_list(lst1, lst2):
    if len(lst1) != len(lst2):
        raise ValueError("Input lists must have the same length")

    if not lst1 or not lst2:
        raise ValueError("Input lists cannot be empty")

    return [x + y for x, y in zip(lst1, lst2)]
import unittest

class Test(unittest.TestCase):
    def test_sum_list(self):
        self.assertEqual(sum_list([10,20,30],[15,25,35]), [25,45,65])

if __name__ == '__main__':
    unittest.main()