def is_woodall(x):
    if x <= 0 or not isinstance(x, int):
        return False
    n = 1
    woodall_num = 1
    while woodall_num < x:
        n += 1
        woodall_num = n * (2*n - 1)
    return woodall_num == x
import unittest

class Test(unittest.TestCase):
    def test_woodall_number(self):
        self.assertEqual(is_woodall(383), True)

if __name__ == '__main__':
    unittest.main()