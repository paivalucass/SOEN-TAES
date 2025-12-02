def pluck(arr):
    smallest_even_value = float('inf')
    smallest_index = -1
    for i in range(len(arr)):
        if arr[i] % 2 == 0 and arr[i] < smallest_even_value:
            smallest_even_value = arr[i]
            smallest_index = i
    if smallest_index == -1:
        return []
    return [smallest_even_value, smallest_index]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test([4,2,3]), [2, 1])

if __name__ == '__main__':
    unittest.main()