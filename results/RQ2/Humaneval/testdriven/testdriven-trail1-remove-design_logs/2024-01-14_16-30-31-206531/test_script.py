def f(n):
    result_lst = []
    for i in range(1, n+1):
        if i % 2 == 0:
            result_lst.append(factorial(i))
        else:
            result_lst.append(sum(range(1, i+1)))
    return result_lst


def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result
import unittest

# Implement the function f that takes n as a parameter,
# and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
# or the sum of numbers from 1 to i otherwise.
# i starts from 1.
# the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test(5), [1, 2, 6, 24, 15])

if __name__ == '__main__':
    unittest.main()