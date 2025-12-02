def find_substring(str_list, sub_str):
    if not isinstance(str_list, list) or not all(isinstance(s, str) for s in str_list) or not isinstance(sub_str, str):
        raise ValueError("Invalid input. Input must be a list of strings and a substring.")

    if not str_list or not sub_str:
        return False

    for string in str_list:
        if sub_str in string:
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_substring(["red", "black", "white", "green", "orange"], "ack"), True)

if __name__ == '__main__':
    unittest.main()