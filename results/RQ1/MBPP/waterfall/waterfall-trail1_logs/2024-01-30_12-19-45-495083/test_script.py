def is_woodall(x):
    if type(x) != int or x <= 0:
        return False
    n = 1
    woodall_num = 0
    while woodall_num < x:
        woodall_num = (2**n - 1) * n
        if woodall_num == x:
            return True
        n += 1
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_woodall(383), True)

if __name__ == '__main__':
    unittest.main()