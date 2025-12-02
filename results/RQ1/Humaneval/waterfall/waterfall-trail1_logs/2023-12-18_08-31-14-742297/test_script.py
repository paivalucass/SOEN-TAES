def file_name_check(file_name):
    import re
    
    if not isinstance(file_name, str):
        return "Invalid input"

    pattern = "^[a-zA-Z][a-zA-Z0-9]*\\.(txt|exe|dll)$"
    if re.match(pattern, file_name):
        return "Yes"
    else:
        return "No"
import unittest

class Test(unittest.TestCase):
    def test_valid_file_name(self):
        self.assertEqual(file_name_check("example.txt"), 'Yes')

    def test_invalid_file_name(self):
        self.assertEqual(file_name_check("1example.dll"), 'No')

if __name__ == '__main__':
    unittest.main()