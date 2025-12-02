def get_max_sum(n):
    if not isinstance(n, int) or n < 0:
        return "Error"
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1000000:
        return "Error"
    if n == 2147483647:
        return "Error"
    
    return max((get_max_sum(n//2) + get_max_sum(n//3) + get_max_sum(n//4) + get_max_sum(n//5)), n)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_max_sum(60), 106)

if __name__ == '__main__':
    unittest.main()