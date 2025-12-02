def find(n, m):
    try:
        if not isinstance(n, (int, float)) or not isinstance(m, (int, float)):
            raise TypeError("Input values must be numerical")
        if m == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        
        return n // m

    except ZeroDivisionError as e:
        return "Error: Division by zero"

    except TypeError as e:
        return "Error: Invalid input, n is not a numerical value"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find(10,3), 3)

if __name__ == '__main__':
    unittest.main()