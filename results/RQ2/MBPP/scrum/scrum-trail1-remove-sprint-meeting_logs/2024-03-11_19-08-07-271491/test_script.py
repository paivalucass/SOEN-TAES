def number_ctr(s):
  count = 0
  for char in s:
    if char.isdigit():
      count += 1
  return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(number_ctr('program2bedone'), 1)

if __name__ == '__main__':
    unittest.main()