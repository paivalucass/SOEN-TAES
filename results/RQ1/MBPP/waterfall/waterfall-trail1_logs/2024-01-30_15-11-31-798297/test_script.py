def odd_length_sum(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        total_sum = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                sub_array = arr[i:j+1]
                if len(sub_array) % 2 != 0:
                    total_sum += sum(sub_array)
        return total_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_length_sum([1,2,4]), 14)

if __name__ == '__main__':
    unittest.main()