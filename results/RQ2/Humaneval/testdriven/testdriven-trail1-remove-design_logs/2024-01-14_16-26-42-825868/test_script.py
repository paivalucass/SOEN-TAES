def tri(n):
    tribonacci = [0, 1, 1]
    if n == 0:
        return tribonacci[:1]
    elif n <= 2:
        return tribonacci[:n+1]
    else:
        for i in range(3, n+1):
            next_num = 1 if i % 2 == 0 else tribonacci[-1] + tribonacci[-2] + tribonacci[-3]
            tribonacci.append(next_num)
        return tribonacci
import unittest

class Test(unittest.TestCase):
    def test_tribonacci(self):
        self.assertEqual(tribonacci(3), [0, 1, 1, 2])

if __name__ == '__main__':
    unittest.main()