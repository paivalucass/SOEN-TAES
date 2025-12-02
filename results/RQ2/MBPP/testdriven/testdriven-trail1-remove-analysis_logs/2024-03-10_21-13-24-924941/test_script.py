def replace_list(original_list, new_list):
    if not isinstance(original_list, list) or not isinstance(new_list, list):
        return "Error: Invalid input, parameters must be lists"
    if not new_list:
        return original_list
    if not original_list:
        return new_list

    original_list.pop()
    original_list.extend(new_list)
    return original_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8]), [1, 3, 5, 7, 9, 2, 4, 6, 8])

if __name__ == '__main__':
    unittest.main()