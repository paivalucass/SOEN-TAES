def pluck(arr):
    smallest_even_value = None
    smallest_even_index = -1

    for i in range(len(arr)):
        if arr[i] % 2 == 0 and (smallest_even_value is None or arr[i] < smallest_even_value):
            smallest_even_value = arr[i]
            smallest_even_index = i

    if smallest_even_value is not None:
        return [smallest_even_value, smallest_even_index]
    else:
        return []
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pluck([4,2,3]), [2, 1])

if __name__ == '__main__':
    unittest.main()