def sequence(n):
    if not isinstance(n, int) or n < 1:
        return "Invalid Input"
    elif n == 1:
        return 1
    else:
        result = [0, 1, 1]
        for i in range(3, n+1):
            result.append(result[result[i-1]] + result[i - result[i-1]])
        if n <= 1000:
            return result[n]
        else:
            return "Some Large Output" if n == 1000 else "Error: Input out of range"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sequence(10), 6)

if __name__ == '__main__':
    unittest.main()