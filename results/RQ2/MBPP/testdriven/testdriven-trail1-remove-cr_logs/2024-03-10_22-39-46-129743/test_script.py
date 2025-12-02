def rearrange_bigger(n):
  if not isinstance(n, int):
    return "Invalid input"

  if n < 0:
    return int(str(n)[0] + ''.join(sorted(str(n)[1:]))[::-1])

  num_list = list(str(n))
  length = len(num_list)

  for i in range(length-1, 0, -1):
    if num_list[i] > num_list[i-1]:
      for j in range(length-1, i-1, -1):
        if num_list[j] > num_list[i-1]:
          num_list[i-1], num_list[j] = num_list[j], num_list[i-1]
          num_list[i:] = sorted(num_list[i:])
          result = int(''.join(num_list))
          return result

  return n
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rearrange_bigger(12), 21)

if __name__ == '__main__':
    unittest.main()