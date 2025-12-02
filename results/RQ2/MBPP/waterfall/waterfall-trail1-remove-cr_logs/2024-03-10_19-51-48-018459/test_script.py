def sequence(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1 or n == 2:
        return 1
    else:
        result = [0] * (n + 1)
        result[1] = 1
        result[2] = 1
        for i in range(3, n + 1):
            result[i] = result[result[i - 1]] + result[i - result[i - 1]]
        return result[n]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sequence(10), 6)

if __name__ == '__main__':
    unittest.main()