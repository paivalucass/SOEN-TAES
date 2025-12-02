def starts_one_ends(n):
    count = 0
    for i in range(10**(n-1), 10**n):
        if str(i)[0] == '1' or str(i)[-1] == '1':
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(starts_one_ends(1), 1)
        self.assertEqual(starts_one_ends(2), 19)
        self.assertEqual(starts_one_ends(3), 271)

if __name__ == '__main__':
    unittest.main()