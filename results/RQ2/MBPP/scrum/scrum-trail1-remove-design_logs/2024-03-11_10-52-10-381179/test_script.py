def my_dict(dict1):
  if isinstance(dict1, dict):
    return bool(dict1)
  else:
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(my_dict({10}), False)

if __name__ == '__main__':
    unittest.main()