def get_max_sum(n, memo={}):
    if n <= 1:
        return n
    elif n in memo:
        return memo[n]
    else:
        memo[n] = max((get_max_sum(n // 2, memo) + get_max_sum(n // 3, memo) + get_max_sum(n // 4, memo) + get_max_sum(n // 5, memo)), n)
        return memo[n]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_max_sum(60), 106)

if __name__ == '__main__':
    unittest.main()