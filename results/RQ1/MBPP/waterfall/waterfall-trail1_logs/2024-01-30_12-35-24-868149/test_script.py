def max_occurrences(nums):
  frequency_dict = {}
  max_freq_num = None
  max_freq = 0
  for number in nums:
    if number in frequency_dict:
      frequency_dict[number] += 1
    else:
      frequency_dict[number] = 1
    if frequency_dict[number] > max_freq:
      max_freq = frequency_dict[number]
      max_freq_num = number
  return max_freq_num
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]), 2)

if __name__ == '__main__':
    unittest.main()