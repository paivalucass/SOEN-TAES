def perimeter_pentagon(a: int) -> int:
    try:
        if type(a) != int or a <= 0:
            raise ValueError("Invalid input")
        return 5 * a
    except ValueError as ve:
        return str(ve)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(perimeter_pentagon(5), 25)

if __name__ == '__main__':
    unittest.main()