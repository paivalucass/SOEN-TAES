def get_positive(l: list) -> list:
    positive_list = []
    for num in l:
        if isinstance(num, (int, float)) and num > 0:
            positive_list.append(num)
    return positive_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])
        self.assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])

if __name__ == '__main__':
    unittest.main()