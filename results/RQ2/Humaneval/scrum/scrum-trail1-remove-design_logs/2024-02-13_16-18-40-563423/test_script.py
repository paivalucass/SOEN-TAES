def is_possible_to_sort_non_decreasing(arr):
    if not arr:
        return True
    sorted_arr = sorted(arr)
    if arr == sorted_arr:
        return True
    return False

def move_one_ball(arr):
    if not arr:
        return True
    sorted_arr = sorted(arr)
    for _ in range(len(arr)):
        if arr == sorted_arr:
            return True
        last_element = arr.pop()
        arr.insert(0, last_element)
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(move_one_ball([3, 4, 5, 1, 2]), True)
        self.assertEqual(move_one_ball([3, 5, 4, 1, 2]), False)

if __name__ == '__main__':
    unittest.main()