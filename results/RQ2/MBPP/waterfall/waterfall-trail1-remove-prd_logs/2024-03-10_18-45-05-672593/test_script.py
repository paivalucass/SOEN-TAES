def move_zero(num_list):
    non_zero_idx = 0
    for i in range(len(num_list)):
        if num_list[i] != 0:
            num_list[i], num_list[non_zero_idx] = num_list[non_zero_idx], num_list[i]
            non_zero_idx += 1
    return num_list

# Testing the function with different input lists
print(move_zero([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]
print(move_zero([0, 0, 0, 1, 2, 3]))  # Output: [1, 2, 3, 0, 0, 0]
print(move_zero([1, 2, 3, 0, 0, 0]))  # Output: [1, 2, 3, 0, 0, 0]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(move_zero([1,0,2,0,3,4]), [1,2,3,4,0,0])

if __name__ == '__main__':
    unittest.main()