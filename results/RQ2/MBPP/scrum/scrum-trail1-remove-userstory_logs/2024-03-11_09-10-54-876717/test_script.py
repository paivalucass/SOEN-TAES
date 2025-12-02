def check_greater(arr, number):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == number:
            return False
        elif arr[mid] < number:
            low = mid + 1
        else:
            high = mid - 1
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_greater([1, 2, 3, 4, 5], 4), False)

if __name__ == '__main__':
    unittest.main()