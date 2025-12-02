def pos_count(input_list):
    if not isinstance(input_list, list) or len(input_list) == 0:
        return "Invalid input. Please provide a non-empty list."

    count = 0
    for num in input_list:
        if isinstance(num, (int, float)):
            if num > 0:
                count += 1
        else:
            return "Invalid input. List should only contain numeric values."

    return count
import unittest

class Test(unittest.TestCase):
    def test_pos_count(self):
        self.assertEqual(pos_count([1, -2, 3, -4]), 2)

if __name__ == '__main__':
    unittest.main()