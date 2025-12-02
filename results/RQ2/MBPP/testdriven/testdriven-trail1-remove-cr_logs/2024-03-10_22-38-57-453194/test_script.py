def get_max_sum(n):
    if n <= 1:
        return n
    return max(n, get_max_sum(n//2) + get_max_sum(n//3) + get_max_sum(n//4) + get_max_sum(n//5))
import unittest

class Test(unittest.TestCase):
    def test_get_max_sum(self):
        self.assertEqual(get_max_sum(60), 106)

if __name__ == '__main__':
    unittest.main()