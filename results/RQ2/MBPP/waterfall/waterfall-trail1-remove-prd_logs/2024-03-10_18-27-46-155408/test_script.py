def is_undulating(n):
  num_str = str(n)
  if len(num_str) < 3:
    return False
  increasing = True
  for i in range(1, len(num_str) - 1):
    if (num_str[i] <= num_str[i - 1] and num_str[i] <= num_str[i + 1]) or (num_str[i] >= num_str[i - 1] and num_str[i] >= num_str[i + 1]):
      increasing = not increasing
  return increasing
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_undulating(1212121), True)

if __name__ == '__main__':
    unittest.main()