def monotonic(l: list):
    increasing = decreasing = True
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            increasing = False
        elif l[i] < l[i + 1]:
            decreasing = False
    return increasing or decreasing
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(monotonic([1, 2, 4, 20]), True)
        self.assertEqual(monotonic([1, 20, 4, 10]), False)
        self.assertEqual(monotonic([4, 1, 0, -10]), True)

if __name__ == '__main__':
    unittest.main()