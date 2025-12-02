def move_zero(num_list):
    '''Write a python function to move all zeroes to the end of the given list.'''
    zero_index = 0
    for i in range(len(num_list)):
        if num_list[i] != 0:
            num_list[zero_index], num_list[i] = num_list[i], num_list[zero_index]
            zero_index += 1
    for i in range(zero_index, len(num_list)):
        num_list[i] = 0
    return num_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(move_zero([1,0,2,0,3,4]), [1,2,3,4,0,0])

if __name__ == '__main__':
    unittest.main()