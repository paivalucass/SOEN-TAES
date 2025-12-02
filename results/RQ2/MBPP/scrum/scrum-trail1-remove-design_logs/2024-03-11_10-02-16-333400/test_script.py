def find_substring(string_list, sub_str):
    if not isinstance(sub_str, str) or not sub_str:
        raise ValueError("sub_str must be a non-empty string")

    for string in string_list:
        if sub_str in string:
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_substring(["red", "black", "white", "green", "orange"],"ack"), True)

if __name__ == '__main__':
    unittest.main()