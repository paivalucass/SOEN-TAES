def re_arrange_array(arr, n):
    if not arr:
        return []

    negative_pointer = 0
    positive_pointer = 0

    while positive_pointer < n:
        if arr[positive_pointer] < 0:
            arr[negative_pointer], arr[positive_pointer] = arr[positive_pointer], arr[negative_pointer]
            negative_pointer += 1
        positive_pointer += 1

    return arr

# Test cases
print(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9)) # Output: [-1, -3, -7, 4, 5, 6, 2, 8, 9]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9), [-1, -3, -7, 4, 5, 6, 2, 8, 9])

if __name__ == '__main__':
    unittest.main()