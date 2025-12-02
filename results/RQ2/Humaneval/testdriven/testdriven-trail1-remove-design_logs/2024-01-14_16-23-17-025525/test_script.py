def closest_integer(value):
    try:
        val = float(value)
        if val % 1 >= 0.5:
            return int(val) + 1 if val > 0 else int(val) - 1
        else:
            return int(round(val))
    except ValueError:
        return "Invalid input value"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(closest_integer('10'), 10)
        self.assertEqual(closest_integer('15.3'), 15)
        self.assertEqual(closest_integer('14.5'), 15)
        self.assertEqual(closest_integer('-14.5'), -15)

if __name__ == '__main__':
    unittest.main()