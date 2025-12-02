def next_power_of_2(n):
    if n < 0:
        raise ValueError("Input should be non-negative")
    
    if not isinstance(n, int):
        raise TypeError("Input should be an integer")
    
    left = 0
    right = n
    while left < right:
        mid = left + (right - left) // 2
        if 2 ** mid < n:
            left = mid + 1
        else:
            right = mid
    
    return 2 ** left
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(next_power_of_2(0), 1)


if __name__ == '__main__':
    unittest.main()