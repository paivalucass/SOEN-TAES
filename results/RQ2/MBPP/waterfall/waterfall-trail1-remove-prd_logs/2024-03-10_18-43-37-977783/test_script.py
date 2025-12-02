def bell_Number(n): 
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")

    bell_num = [0] * (n+1)
    bell_num[0] = 1

    for i in range(1, n+1):
        bell_num[i] = bell_num[i-1]
        for j in range(i-1, 0, -1):
            bell_num[j] += bell_num[j-1]

    return bell_num[n]

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(bell_Number(2), 2)

if __name__ == '__main__':
    unittest.main()