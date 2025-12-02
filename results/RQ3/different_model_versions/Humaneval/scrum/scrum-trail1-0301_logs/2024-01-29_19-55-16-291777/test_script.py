def monotonic(l: list) -> bool:
    if len(l) < 2:
        return True
    increasing = decreasing = True
    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            decreasing = False
        elif l[i] < l[i-1]:
            increasing = False
        if not increasing and not decreasing:
            return False
    return True

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(monotonic([1, 2, 4, 20]))
        self.assertFalse(monotonic([1, 20, 4, 10]))
        self.assertTrue(monotonic([4, 1, 0, -10]))

if __name__ == '__main__':
    unittest.main()