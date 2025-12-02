def odd_length_sum(arr):
    if not arr or not all(isinstance(x, int) for x in arr):
        return 0

    total_sum = 0
    array_length = len(arr)

    for start_index in range(array_length):
        for end_index in range(start_index, array_length, 2):
            for index in range(start_index, end_index + 1):
                total_sum += arr[index]

    return total_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_length_sum([1,2,4]), 14)

if __name__ == '__main__':
    unittest.main()