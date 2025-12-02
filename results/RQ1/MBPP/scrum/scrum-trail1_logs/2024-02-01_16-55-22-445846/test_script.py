def right_insertion(a, x):
    if not isinstance(a, list) or not all(isinstance(i, (int, float)) for i in a) or not isinstance(x, (int, float)):
        return -1
    if not a:
        return 0
    if x in a:
        return a.index(x)
    for i in range(len(a)):
        if a[i] > x:
            return i
    return len(a)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(right_insertion([1,2,4,5], 6), 4)

if __name__ == '__main__':
    unittest.main()