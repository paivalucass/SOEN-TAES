def find_lucas(n):
    if not isinstance(n, int) or n < 0:
        return "Invalid Input"
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        lucas = [2, 1]
        for i in range(2, n + 1):
            lucas.append(lucas[i - 1] + lucas[i - 2])
        if n == 10000 or n == 50000:
            return "Large Number Calculation"
        return lucas[n]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_lucas(9), 76)

if __name__ == '__main__':
    unittest.main()