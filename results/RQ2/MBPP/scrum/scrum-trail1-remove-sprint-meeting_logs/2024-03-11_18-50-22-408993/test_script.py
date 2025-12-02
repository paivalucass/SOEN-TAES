def check_Consecutive(l):
    if not l:
        return False
    else:
        return all((l[i] == l[i + 1] - 1) for i in range(len(l) - 1))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_Consecutive([1,2,3,4,5]), True)

if __name__ == '__main__':
    unittest.main()