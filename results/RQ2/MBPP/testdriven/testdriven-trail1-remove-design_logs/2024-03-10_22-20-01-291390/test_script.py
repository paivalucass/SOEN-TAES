def sum_odd(l, r):
    if l > r or l < 0 or r < 0:
        return "Invalid Input"
    
    total = 0
    for i in range(l, r+1):
        if i % 2 != 0:
            total += i
    return total
import unittest

class Test(unittest.TestCase):
    def test_sum_odd(self):
        self.assertEqual(sum_odd(2, 5), 8)

if __name__ == '__main__':
    unittest.main()