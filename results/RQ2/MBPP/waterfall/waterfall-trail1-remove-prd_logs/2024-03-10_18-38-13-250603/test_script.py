def check_greater(arr, number):
    if not arr:
        raise ValueError("Array should not be empty")

    max_element = max(arr)
    return number > max_element
import unittest

class Test(unittest.TestCase):
    def test_check_greater(self):
        self.assertEqual(check_greater([1, 2, 3, 4, 5], 4), False)

if __name__ == '__main__':
    unittest.main()