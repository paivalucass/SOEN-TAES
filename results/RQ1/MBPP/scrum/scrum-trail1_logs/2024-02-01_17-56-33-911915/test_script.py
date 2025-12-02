def newman_prime(n):
  if n == 1:
    return 7
  elif n == 2:
    return 11
  else:
    num = 7
    count = 2
    while count < n:
      num += 10
      if is_prime(num) and is_prime(2**num - 1):
        count += 1
    return num

# Helper function to check if a number is prime
# You can implement this function separately

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(newman_prime(3), 7)

if __name__ == '__main__':
    unittest.main()