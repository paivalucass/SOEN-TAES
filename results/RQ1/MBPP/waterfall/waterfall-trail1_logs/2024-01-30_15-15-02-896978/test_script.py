def sum_odd(l, r):
    if not isinstance(l, int) or not isinstance(r, int) or l < 0 or r < 0:
        return "Left and right boundaries should be non-negative integers"
    
    if l > r:
        return "Left boundary should not be greater than right boundary"
    
    if l % 2 == 0:
        l += 1
    
    if r % 2 == 0:
        r -= 1
    
    count = (r - l) // 2 + 1
    total_sum = count * (l + r) // 2
    return total_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_odd(2, 5), 8)

if __name__ == '__main__':
    unittest.main()