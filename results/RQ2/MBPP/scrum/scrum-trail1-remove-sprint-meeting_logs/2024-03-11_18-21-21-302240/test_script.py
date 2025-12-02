def search(arr):
    if not arr or len(arr) == 0:
        return "Error"

    if len(arr) == 1:
        return arr[0]

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if mid == 0 and arr[mid] != arr[mid + 1]:
            return arr[mid]
        elif mid == len(arr) - 1 and arr[mid] != arr[mid - 1]:
            return arr[mid]
        elif arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
            return arr[mid]
        elif arr[mid] == arr[mid - 1]:
            if (mid - 1 - left) % 2 == 0:
                left = mid + 1
            else:
                right = mid - 2
        else:
            if (right - mid - 1) % 2 == 0:
                right = mid - 1
            else:
                left = mid + 2
    return "Error"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(search([1,1,2,2,3]), 3)

if __name__ == '__main__':
    unittest.main()