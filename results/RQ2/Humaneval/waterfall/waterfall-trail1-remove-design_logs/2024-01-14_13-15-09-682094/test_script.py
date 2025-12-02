def closest_integer(value):
    if '.' in value:
        val = float(value)
        if val > 0:
            return int(val + 0.5)
        else:
            return int(val - 0.5)
    else:
        return int(value)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(closest_integer('10'), 10)
        self.assertEqual(closest_integer('15.3'), 15)
        self.assertEqual(closest_integer('14.5'), 15)
        self.assertEqual(closest_integer('-14.5'), -15)

if __name__ == '__main__':
    unittest.main()