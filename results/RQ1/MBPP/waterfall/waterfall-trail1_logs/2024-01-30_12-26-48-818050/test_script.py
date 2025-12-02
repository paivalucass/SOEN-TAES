def find_substring(string_list, substring):
    if not isinstance(string_list, list) or not all(isinstance(s, str) for s in string_list) or not isinstance(substring, str):
        raise ValueError("Input validation failed. string_list must be a list of strings and substring must be a string.")

    for s in string_list:
        if substring.lower() in s.lower():
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_substring(["red", "black", "white", "green", "orange"],"ack"), True)

if __name__ == '__main__':
    unittest.main()