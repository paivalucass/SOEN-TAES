def left_insertion(sorted_list, value):
    if len(sorted_list) == 0:
        return 0
    left, right = 0, len(sorted_list)
    while left < right:
        mid = (left + right) // 2
        if sorted_list[mid] < value:
            left = mid + 1
        else:
            right = mid
    return left
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(left_insertion([1, 2, 4, 5], 6), 4)

if __name__ == '__main__':
    unittest.main()