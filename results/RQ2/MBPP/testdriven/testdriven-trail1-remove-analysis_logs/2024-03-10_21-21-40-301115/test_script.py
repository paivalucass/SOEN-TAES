def check_Consecutive(l):
    if not isinstance(l, list) or len(l) < 2:
        return False

    for i in range(1, len(l)):
        if not isinstance(l[i], int) or l[i] != l[i-1] + 1:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_Consecutive([1,2,3,4,5]), True)

if __name__ == '__main__':
    unittest.main()