def f(n):
    result = []
    factorial_memo = {}
    sum_memo = {}

    def factorial(num):
        if num in factorial_memo:
            return factorial_memo[num]
        if num == 0 or num == 1:
            return 1
        factorial_memo[num] = num * factorial(num - 1)
        return factorial_memo[num]

    def calculate_sum(num):
        if num in sum_memo:
            return sum_memo[num]
        sum_val = 0
        for i in range(1, num + 1):
            sum_val += i
        sum_memo[num] = sum_val
        return sum_val

    for i in range(1, n + 1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(calculate_sum(i))

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f(5), [1, 2, 6, 24, 15])

if __name__ == '__main__':
    unittest.main()