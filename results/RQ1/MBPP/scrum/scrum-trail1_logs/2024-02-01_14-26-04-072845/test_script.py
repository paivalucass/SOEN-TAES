def find_substring(str1, sub_str):
    def kmp_search(text, pattern):
        # KMP search algorithm implementation
        # ...
        return True if pattern in text else False

    for string in str1:
        if kmp_search(string, sub_str):
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_substring(["red", "black", "white", "green", "orange"],"ack"), True)

if __name__ == '__main__':
    unittest.main()