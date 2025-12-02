def find(n, m):
    try:
        if m == 0:
            raise ZeroDivisionError
        else:
            result = n // m
            return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find(10, 3), 3)

if __name__ == '__main__':
    unittest.main()