def get_pairs_count(arr, sum):
    '''Write a python function to count the number of pairs whose sum is equal to ‘sum’. The function gets as input a list of numbers and the sum.
    '''
    # Write your code here
    pair_count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == sum:
                pair_count += 1
    return pair_count

assert get_pairs_count([1,1,1,1],2) == 6
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_pairs_count([1,1,1,1], 2), 6)

if __name__ == '__main__':
    unittest.main()