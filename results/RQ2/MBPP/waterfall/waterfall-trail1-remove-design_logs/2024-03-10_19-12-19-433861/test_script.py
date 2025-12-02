def find(n, m):
    try:
        if m == 0:
            raise ZeroDivisionError("Error: Division by Zero")
        return n // m
    except ZeroDivisionError as e:
        return "Error: Division by Zero"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find(10, 3), 3)

if __name__ == '__main__':
    unittest.main()