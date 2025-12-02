def check_Consecutive(l):
    if len(l) < 2:
        return True
    else:
        return all(x == y - 1 for x, y in zip(l, l[1:]))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_Consecutive([1,2,3,4,5]), True)

if __name__ == '__main__':
    unittest.main()