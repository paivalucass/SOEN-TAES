def catalan_number(num):
    memo = {}
    
    if num <= 1:
        return 1
    elif num in memo:
        return memo[num]
    else:
        result = 0
        for i in range(num):
            result += catalan_number(i) * catalan_number(num - i - 1)
        memo[num] = result
        return result
import unittest

class Test(unittest.TestCase):
    def test_catalan_number(self):
        self.assertEqual(catalan_number(10), 16796)

if __name__ == '__main__':
    unittest.main()