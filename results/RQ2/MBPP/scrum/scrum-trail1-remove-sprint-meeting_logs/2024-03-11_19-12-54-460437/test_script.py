def remove_nested(test_tup):
  new_tup = []
  for item in test_tup:
    if isinstance(item, tuple):
      new_tup.extend(item)
    else:
      new_tup.append(item)
  return tuple(new_tup)
import unittest

class Test(unittest.TestCase):
    def test_remove_nested(self):
        self.assertEqual(remove_nested((1, 5, 7, (4, 6), 10)), (1, 5, 7, 10))

if __name__ == '__main__':
    unittest.main()