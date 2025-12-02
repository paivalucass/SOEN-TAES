def move_zero(num_list):
    if not isinstance(num_list, list):
        return "Error: Input is not a list"
    if not all(isinstance(num, (int, float)) for num in num_list):
        return "Error: List contains non-numeric elements"
    
    zero_count = num_list.count(0)
    num_list = [num for num in num_list if num != 0]
    num_list.extend([0] * zero_count)
    return num_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(move_zero([1,0,2,0,3,4]), [1,2,3,4,0,0])

if __name__ == '__main__':
    unittest.main()