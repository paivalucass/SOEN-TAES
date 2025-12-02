def check_greater(arr, number):
    if not arr:
        return False
    for element in arr:
        if number >= element:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_greater([1, 2, 3, 4, 5], 4), False)

if __name__ == '__main__':
    unittest.main()