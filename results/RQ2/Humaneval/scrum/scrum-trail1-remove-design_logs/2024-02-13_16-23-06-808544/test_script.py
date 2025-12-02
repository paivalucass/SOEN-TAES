def tri(n):
    tribonacci = [0, 1, 1]
    for i in range(3, n+1):
        tribonacci.append(tribonacci[i-1] + tribonacci[i-2] + tribonacci[i-3])
    return tribonacci[:n+1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tri(3), [0, 1, 1, 2])

if __name__ == '__main__':
    unittest.main()