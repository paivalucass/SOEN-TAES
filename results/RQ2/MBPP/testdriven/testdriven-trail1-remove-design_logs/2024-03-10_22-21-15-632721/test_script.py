def get_ludic(n):
    if not isinstance(n, int) or n <= 1:
        return "Error: Invalid input data"
    
    result = []
    num = 1
    while num <= n:
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            result.append(num)
        num += 1
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_ludic(10), [1, 2, 3, 5, 7])

if __name__ == '__main__':
    unittest.main()