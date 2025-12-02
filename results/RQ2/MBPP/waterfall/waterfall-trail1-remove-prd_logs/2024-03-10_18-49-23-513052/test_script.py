def right_insertion(a, x):
    if len(a) == 0 or x > a[-1]:
        return len(a)
    elif x < a[0]:
        return 0
    elif x in a:
        return a.index(x)
    else:
        for i in range(len(a)):
            if a[i] >= x:
                return i
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(right_insertion([1,2,4,5], 6), 4)

if __name__ == '__main__':
    unittest.main()