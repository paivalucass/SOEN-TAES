def max_element(l: list):
    if not l:
        return []
    elif all(isinstance(i, (int, float)) for i in l):
        max_num = max(l)
        max_elements = [i for i in l if i == max_num]
        return max_num if len(max_elements) == 1 else max_elements
    else:
        return "Invalid Input"
import unittest

class Test(unittest.TestCase):
    def test_max_element(self):
        self.assertEqual(max_element([1, 2, 3]), 3)
        self.assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)

if __name__ == '__main__':
    unittest.main()