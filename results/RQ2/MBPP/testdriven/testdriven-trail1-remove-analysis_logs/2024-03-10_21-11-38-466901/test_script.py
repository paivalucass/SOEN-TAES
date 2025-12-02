def pancake_sort(nums):
    def flip(sublist, k):
        i = 0
        while i < k / 2:
            sublist[i], sublist[k - i - 1] = sublist[k - i - 1], sublist[i]
            i += 1

    def find_max_index(sublist, k):
        max_index = 0
        for i in range(k):
            if sublist[i] > sublist[max_index]:
                max_index = i
        return max_index

    n = len(nums)
    for i in range(n - 1, 0, -1):
        max_index = find_max_index(nums, i + 1)
        if max_index != i:
            flip(nums, max_index + 1)
            flip(nums, i + 1)

    return nums

# Test case
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
import unittest

class Test(unittest.TestCase):
    def test_pancake_sort(self):
        self.assertEqual(pancake_sort([15, 79, 25, 38, 69]), [15, 25, 38, 69, 79])

if __name__ == '__main__':
    unittest.main()