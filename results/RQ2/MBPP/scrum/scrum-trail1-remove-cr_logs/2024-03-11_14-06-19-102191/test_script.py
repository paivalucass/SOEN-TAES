def sum_odd(l, r):
    if l > r or l < 0 or r < 0 or not isinstance(l, int) or not isinstance(r, int):
        return "Invalid input"
    else:
        result = 0
        for i in range(l, r+1):
            if i % 2 != 0:
                result += i
        return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_odd(2, 5), 8)

if __name__ == '__main__':
    unittest.main()