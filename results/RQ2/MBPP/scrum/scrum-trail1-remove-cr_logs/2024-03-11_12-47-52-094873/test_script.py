def find_solution(a, b, n):
    if isinstance(a, int) and isinstance(b, int) and isinstance(n, int):
        for x in range(0, n + 1):
            for y in range(0, n + 1):
                if a * x + b * y == n:
                    return (x, y)
        return None
    else:
        return "Invalid input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_solution(2, 3, 7), (2, 1))

if __name__ == '__main__':
    unittest.main()