def tri(n):
    if not isinstance(n, int) or n < 0:
        return 'Invalid input: n must be a non-negative integer.'
    else:
        result = [0, 1, 1]
        for i in range(3, n + 1):
            if i % 2 == 0:
                result.append(1 + i // 2)
            else:
                result.append(result[i - 1] + result[i - 2] + result[i - 3])
        return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tri(3), [1, 3, 2, 8])

if __name__ == '__main__':
    unittest.main()