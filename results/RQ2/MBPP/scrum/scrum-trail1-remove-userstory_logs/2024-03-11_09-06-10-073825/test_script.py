def find(n, m):
    assert isinstance(n, int) and isinstance(m, int)
    try:
        if m == 0:
            raise ZeroDivisionError
        return n // m
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except Exception as e:
        return "An error occurred: " + str(e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find(10, 3), 3)

if __name__ == '__main__':
    unittest.main()