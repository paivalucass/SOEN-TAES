def bell_Number(n):
    bell = [0] * (n+1)
    bell[0] = 1
    for i in range(1, n+1):
        bell[i] = bell[i-1]
        for j in range(i-1, 0, -1):
            bell[j] += bell[j-1]
    return bell[n-1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(bell_Number(2), 2)

if __name__ == '__main__':
    unittest.main()