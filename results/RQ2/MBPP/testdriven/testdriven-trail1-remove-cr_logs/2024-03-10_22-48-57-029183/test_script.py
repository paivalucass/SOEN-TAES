def move_zero(num_list):
    non_zero_elements = [x for x in num_list if x != 0]
    zero_elements = [x for x in num_list if x == 0]
    return non_zero_elements + zero_elements

assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(move_zero([1,0,2,0,3,4]), [1,2,3,4,0,0])

if __name__ == '__main__':
    unittest.main()