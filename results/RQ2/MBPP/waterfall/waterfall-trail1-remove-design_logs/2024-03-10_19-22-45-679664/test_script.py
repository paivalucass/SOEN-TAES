def move_zero(num_list):
    zero_count = num_list.count(0)
    non_zero_list = [num for num in num_list if num != 0]
    non_zero_list.extend([0] * zero_count)
    return non_zero_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(move_zero([1,0,2,0,3,4]), [1,2,3,4,0,0])

if __name__ == '__main__':
    unittest.main()