def find_solution(a, b, n):
    for x in range(n + 1):
        if a * x > n:
            break
        if (n - a * x) % b == 0:
            y = (n - a * x) // b
            return (x, y)
    return None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_solution(2, 3, 7), (2, 1))

if __name__ == '__main__':
    unittest.main()