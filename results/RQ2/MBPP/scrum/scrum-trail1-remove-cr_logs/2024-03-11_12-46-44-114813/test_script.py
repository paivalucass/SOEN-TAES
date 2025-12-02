def pancake_sort(nums):
    def flip(arr, k):
        i = 0
        while i < k / 2:
            arr[i], arr[k - i - 1] = arr[k - i - 1], arr[i]
            i += 1

    def pancakeSort(arr):
        cur = len(arr)
        while cur > 1:
            maxIndex = arr.index(max(arr[0:cur]))
            flip(arr, maxIndex + 1)
            flip(arr, cur)
            cur -= 1
        return arr

    return pancakeSort(nums)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pancake_sort([15, 79, 25, 38, 69]), [15, 25, 38, 69, 79])

if __name__ == '__main__':
    unittest.main()