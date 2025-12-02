def get_pairs_count(arr, sum):
    '''
    Write a python function to count the number of pairs whose sum is equal to ‘sum’.
    The function gets as input a list of numbers and the sum
    '''
    pair_count = 0
    num_counts = {}

    for num in arr:
        complement = sum - num
        if complement in num_counts:
            pair_count += num_counts[complement]

        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1

    return pair_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_pairs_count([1,1,1,1], 2), 6)

if __name__ == '__main__':
    unittest.main()