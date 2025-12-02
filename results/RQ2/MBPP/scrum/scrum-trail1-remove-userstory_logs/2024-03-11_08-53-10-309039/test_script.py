def is_undulating(n):
  n_str = str(n)
  if len(n_str) < 3:
    return False
  for i in range(2, len(n_str)):
    if (n_str[i] == n_str[i-2]) and (n_str[i-1] != n_str[i]):
      continue
    elif (n_str[i] != n_str[i-2]) and (n_str[i-1] == n_str[i]):
      continue
    else:
      return False
  return True
import unittest

class Test(unittest.TestCase):
    def test_is_undulating(self):
        self.assertEqual(is_undulating(1212121), True)

if __name__ == '__main__':
    unittest.main()