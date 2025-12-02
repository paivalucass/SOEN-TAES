def re_arrange_array(arr, n):
    if n <= 0 or n > len(arr):
        return "Invalid input for n"

    # Rearrange the array
    left = 0
    right = n - 1

    while left < right:
        if arr[left] < 0:
            left += 1
        else:
            if arr[right] < 0:
                arr[left], arr[right] = arr[right], arr[left]
            right -= 1

    return arr
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9), [-1, -3, -7, 4, 5, 6, 2, 8, 9])

if __name__ == '__main__':
    unittest.main()