def get_odd_collatz(n):
    result = [n]
    while n > 1:
        n = n * 3 + 1 if n % 2 else n // 2
        if n % 2 != 0 and n != 1:
            result.append(n)
        if n == 1:
            break
    return sorted(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_odd_collatz(5), [1, 5])

if __name__ == '__main__':
    unittest.main()