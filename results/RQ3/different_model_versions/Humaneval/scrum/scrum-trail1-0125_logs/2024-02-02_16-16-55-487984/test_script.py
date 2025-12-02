def monotonic(l: list) -> bool:
    if len(l) < 2:
        return True

    def is_monotonic(l: list, start: int, end: int) -> bool:
        if start >= end:
            return True
        mid = (start + end) // 2
        
        if l[mid] < l[mid+1]:
            return is_monotonic(l, mid+1, end)
        elif l[mid] > l[mid+1]:
            return is_monotonic(l, start, mid)
        
        return False
        
    return is_monotonic(l, 0, len(l)-1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(monotonic([1, 2, 4, 20]))
        self.assertFalse(monotonic([1, 20, 4, 10]))
        self.assertTrue(monotonic([4, 1, 0, -10]))

if __name__ == '__main__':
    unittest.main()