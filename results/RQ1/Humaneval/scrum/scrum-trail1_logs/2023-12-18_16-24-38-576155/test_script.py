def closest_integer(value):
  try:
    num = float(value)
    if num < 0:
      return int(num - 0.5)
    else:
      return int(num + 0.5)
  except ValueError:
    return 'Invalid input'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(closest_integer('10'), 10)
        self.assertEqual(closest_integer('15.3'), 15)
        self.assertEqual(closest_integer('14.5'), 15)
        self.assertEqual(closest_integer('-14.5'), -15)

if __name__ == '__main__':
    unittest.main()