def odd_length_sum(arr):
    result = 0
    for i in range(len(arr)):
        for j in range(i, len(arr), 2):
            for k in range(i, j+1):
                result += arr[k]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_length_sum([1,2,4]), 14)

if __name__ == '__main__':
    unittest.main()