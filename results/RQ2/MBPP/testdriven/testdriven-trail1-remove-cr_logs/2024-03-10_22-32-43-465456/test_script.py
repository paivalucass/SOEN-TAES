def find_solution(a, b, n):
    for x in range(n+1):
        y = (n - (a * x)) / b
        if y.is_integer() and y >= 0:
            return (x, int(y))
    return None
import unittest

class Test(unittest.TestCase):
    def test_find_solution(self):
        self.assertEqual(find_solution(2, 3, 7), (2, 1))

if __name__ == '__main__':
    unittest.main()