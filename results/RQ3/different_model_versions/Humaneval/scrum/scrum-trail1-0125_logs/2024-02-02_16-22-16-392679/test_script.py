def closest_integer(value):
    num = float(value)
    if num % 1 < 0.5:
        return int(num)
    elif num > 0:
        return int(num) + 1
    else:
        return int(num) - 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(closest_integer('10'), 10)
        self.assertEqual(closest_integer('15.3'), 15)
        self.assertEqual(closest_integer('14.5'), 15)
        self.assertEqual(closest_integer('-14.5'), -15)

if __name__ == '__main__':
    unittest.main()