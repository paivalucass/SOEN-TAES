def largest_subset(a):
    '''
    Write a function to find the size of the largest subset of a list of numbers so that every pair is divisible.
    assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
    '''
    subset_sizes = {}
    max_subset_size = 0
    a.sort()
    for i in a:
        current_subset_size = 1
        for j in a[:a.index(i)]:
            if i % j == 0:
                current_subset_size = max(current_subset_size, subset_sizes[j] + 1)
        subset_sizes[i] = current_subset_size
        max_subset_size = max(max_subset_size, current_subset_size)
    return max_subset_size
import unittest

class Test(unittest.TestCase):
    def test_largest_subset(self):
        self.assertEqual(largest_subset([1, 3, 6, 13, 17, 18]), 4)

if __name__ == '__main__':
    unittest.main()