def sequence(n):
    if not isinstance(n, int) or n < 1:
        return "Invalid Input"
    
    if n == 1:
        return 1
    if n == 2:
        return 1
    
    seq = [0] * (n + 1)
    seq[1] = 1
    seq[2] = 1

    for i in range(3, n + 1):
        seq[i] = seq[seq[i - 1]] + seq[i - seq[i - 1]]

    return seq[n]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sequence(10), 6)

if __name__ == '__main__':
    unittest.main()