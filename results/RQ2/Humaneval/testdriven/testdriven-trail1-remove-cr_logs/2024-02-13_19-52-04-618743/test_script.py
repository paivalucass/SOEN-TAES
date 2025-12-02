def tri(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]

    result = [0, 1, 1]
    for i in range(3, n + 1):
        if i % 2 == 0:
            result.append(1 + i // 2)
        else:
            result.append(result[i - 1] + result[i - 2] + result[i - 3])

    return result
import unittest

class Test(unittest.TestCase):
    def test_tribonacci(self):
        self.assertEqual(tribonacci(3), [0, 1, 1, 2])
        self.assertEqual(tribonacci(4), [0, 1, 1, 2, 4])
        self.assertEqual(tribonacci(5), [0, 1, 1, 2, 4, 7])

if __name__ == '__main__':
    unittest.main()