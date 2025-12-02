def split_two_parts(input_list, split_index):
    first_part_of_list = input_list[:split_index]
    second_part_of_list = input_list[split_index:]
    return (first_part_of_list, second_part_of_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(split_two_parts([1,1,2,3,4,4,5,1], 3), ([1, 1, 2], [3, 4, 4, 5, 1]))

if __name__ == '__main__':
    unittest.main()