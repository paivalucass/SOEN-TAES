def monotonic(l: list):
    if len(l) == 0:
        return True
    elif all(l[i] <= l[i + 1] for i in range(len(l) - 1)) or all(l[i] >= l[i + 1] for i in range(len(l) - 1)):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(monotonic([1, 2, 4, 20]), True)
        self.assertEqual(monotonic([1, 20, 4, 10]), False)
        self.assertEqual(monotonic([4, 1, 0, -10]), True)

if __name__ == '__main__':
    unittest.main()