def move_one_ball(arr):
    if len(arr) == 0:
        return True
    else:
        return sorted(arr) == arr or sorted(arr[-1:] + arr[:-1]) == arr or sorted(arr[-2:] + arr[:-2]) == arr or sorted(arr[-3:] + arr[:-3]) == arr or sorted(arr[-4:] + arr[:-4]) == arr
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(move_one_ball([3, 4, 5, 1, 2]), True)
        self.assertEqual(move_one_ball([3, 5, 4, 1, 2]), False)

if __name__ == '__main__':
    unittest.main()