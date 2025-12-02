def add_elements(arr, k):
    """
    Given a non-empty array of integers array and an integer k, return
    the sum of the elements with at most two digits from the first k elements of array.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """

    total_sum = 0
    for num in arr[:k]:
        if abs(num) < 100:
            total_sum += num
    return total_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_elements([111,21,3,4000,5,6,7,8,9], 4), 24)

if __name__ == '__main__':
    unittest.main()