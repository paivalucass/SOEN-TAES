def tri(n):
    tribonacci = [0, 1, 1]
    if n == 0:
        return []
    elif n == 1:
        return [tribonacci[0]]
    elif n == 2:
        return tribonacci[:2]
    else:
        for i in range(3, n + 1):
            tribonacci.append(tribonacci[i - 1] + tribonacci[i - 2] + tribonacci[i - 3])
        return tribonacci
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tri(0), [])
        self.assertEqual(tri(1), [3])
        self.assertEqual(tri(2), [3, 1])
        self.assertEqual(tri(3), [3, 1, 2, 8])
        self.assertEqual(tri(4), [3, 1, 2, 8, 4])

if __name__ == '__main__':
    unittest.main()