def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

def sum_up_to(num):
    return sum(range(1, num + 1))

def f(n):
    result = []
    if n < 0:
        return ["Error: Invalid input"]
    if n > 100:
        return ["Error: Number too large"]
    for i in range(1, n + 1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(sum_up_to(i))
    return result
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test(5), [1, 2, 6, 24, 15])

if __name__ == '__main__':
    unittest.main()