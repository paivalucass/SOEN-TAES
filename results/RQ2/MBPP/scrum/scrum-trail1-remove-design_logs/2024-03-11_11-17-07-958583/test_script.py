def right_insertion(a, x):
    if not isinstance(x, int):
        return "Error"
    if x < a[0]:
        return 0
    elif x > a[-1]:
        return len(a)
    else:
        for i in range(len(a)):
            if a[i] < x <= a[i + 1]:
                return i + 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(right_insertion([1,2,4,5], 6), 4)

if __name__ == '__main__':
    unittest.main()