def last_Digit(n):
    try:
        if isinstance(n, (int, float)):
            last = int(str(n)[-1])
            return last
        else:
            raise ValueError("Error: Non-numeric input")
    except ValueError as e:
        return str(e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(last_Digit(123), 3)

if __name__ == '__main__':
    unittest.main()