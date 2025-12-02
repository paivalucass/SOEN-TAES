def rearrange_bigger(*args):
  '''Write a function to create the next bigger number by rearranging the digits of a given number.
  assert rearrange_bigger(12)==21'''
  num_str = str(args[0])
  num_list = list(num_str)
  num_list.sort(reverse=True)
  return int(''.join(num_list))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rearrange_bigger(12), 21)

if __name__ == '__main__':
    unittest.main()