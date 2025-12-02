def find_substring(str_list, sub_str):
    if not isinstance(str_list, list) or not all(isinstance(i, str) for i in str_list) or not isinstance(sub_str, str):
        raise TypeError("Input validation failed. Please ensure str_list is a list of strings and sub_str is a string.")

    if not str_list or not sub_str:
        return False

    for string in str_list:
        if sub_str in string:
            return True

    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_substring(["red", "black", "white", "green", "orange"],"ack"), True)

if __name__ == '__main__':
    unittest.main()