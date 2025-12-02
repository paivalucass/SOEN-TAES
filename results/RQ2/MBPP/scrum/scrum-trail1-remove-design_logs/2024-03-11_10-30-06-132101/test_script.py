def get_max_sum(n):
    if n <= 0:
        return 0
    if n <= 5:
        return n
    return max(get_max_sum(n//2) + get_max_sum(n//3) + get_max_sum(n//4) + get_max_sum(n//5), n)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test(60), 106)

if __name__ == '__main__':
    unittest.main()