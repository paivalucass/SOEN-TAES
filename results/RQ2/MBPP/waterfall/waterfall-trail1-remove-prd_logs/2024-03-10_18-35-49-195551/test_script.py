def find_lucas(n):
    memoization_table = {}

    def lucas_helper(n):
        if n in memoization_table:
            return memoization_table[n]
        if n == 0:
            return 2
        elif n == 1:
            return 1
        else:
            result = lucas_helper(n-1) + lucas_helper(n-2)
            memoization_table[n] = result
            return result

    return lucas_helper(n)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_lucas(9), 76)

if __name__ == '__main__':
    unittest.main()