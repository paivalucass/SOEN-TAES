def remove_nested(test_tup):
  result = []
  for x in test_tup:
    if isinstance(x, tuple):
      result.extend(remove_nested(x))
    else:
      result.append(x)
  return tuple([x for x in result if not isinstance(x, tuple)])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_nested((1, 5, 7, (4, 6), 10)), (1, 5, 7, 10))

if __name__ == '__main__':
    unittest.main()