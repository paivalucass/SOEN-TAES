def get_max_sum(n):
    cache = {}

    def helper(n):
        if n in cache:
            return cache[n]

        if n <= 1:
            return n

        max_sum = max(helper(n//2), helper(n//3), helper(n//4), helper(n//5), n)
        cache[n] = max_sum
        return max_sum

    return helper(n)
import unittest

class Test(unittest.TestCase):
    def test_get_max_sum(self):
        self.assertEqual(get_max_sum(60), 106)

if __name__ == '__main__':
    unittest.main()