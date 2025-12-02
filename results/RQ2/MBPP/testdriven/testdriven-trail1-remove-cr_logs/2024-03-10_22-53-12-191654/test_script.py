def find_sum(arr):
    """
    Function to find the sum of non-repeated elements in a given list.

    Args:
    arr (list): Input list of integers.

    Returns:
    int: Sum of the non-repeated elements in the input list.
    """
    frequency = {}
    sum_non_repeated = 0

    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    for key, value in frequency.items():
        if value == 1:
            sum_non_repeated += key

    return sum_non_repeated
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_sum([1,2,3,1,1,4,5,6]), 21)

if __name__ == '__main__':
    unittest.main()