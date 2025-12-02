def move_zero(num_list):
    '''
    Write a python function to move all zeroes to the end of the given list.
    assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
    '''
    left_pointer = 0
    right_pointer = 0
    # Iterate through the list to move zeroes to the end
    while right_pointer < len(num_list):
        if num_list[right_pointer] != 0:
            # Swap non-zero element with the left pointer
            num_list[left_pointer], num_list[right_pointer] = num_list[right_pointer], num_list[left_pointer]
            left_pointer += 1
        right_pointer += 1
    return num_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(move_zero([1,0,2,0,3,4]), [1,2,3,4,0,0])

if __name__ == '__main__':
    unittest.main()