def count_no_of_ways(n, k):
    '''
    Write a function to find out the number of ways of painting the fence such that at most 2 adjacent posts have the same color for the given fence with n posts and k colors.
    assert count_no_of_ways(2, 4) == 16
    '''
    if n == 0:
        return 1  # base case
    same = 0  # number of ways to paint the last two posts the same
    diff = k  # number of ways to paint the last two posts different
    total = same + diff  # total number of ways to paint the last two posts
    for _ in range(2, n+1):
        same, diff = diff, (total * (k-1))  # update same and diff based on previous total
        total = same + diff  # update total based on new same and diff
    return total  # return the total number of ways to paint the entire fence

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_no_of_ways(2, 4), 16)

if __name__ == '__main__':
    unittest.main()