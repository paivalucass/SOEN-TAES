def find(n, m):
    if not isinstance(n, (int, float)) or not isinstance(m, (int, float)):
        return "Error: Invalid input. Please enter valid numbers for n and m."

    try:
        result = int(n // m)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except OverflowError:
        return "Error: Result too large to handle"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find(10, 3), 3)

if __name__ == '__main__':
    unittest.main()