def check_greater(arr, number):
    if not isinstance(arr, list) or not isinstance(number, (int, float)):
        return False

    if len(arr) == 0:
        return False
    
    for element in arr:
        if number <= element:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test_check_greater(self):
        self.assertEqual(check_greater([1, 2, 3, 4, 5], 4), False)

if __name__ == '__main__':
    unittest.main()