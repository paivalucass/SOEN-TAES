def file_name_check(file_name):
    import re

    allowed_extensions = ['txt', 'exe', 'dll']

    if file_name.count('.') != 1:
        return 'No'
    
    name, ext = file_name.rsplit('.', 1)
    
    if ext not in allowed_extensions or not re.match(r'^[a-zA-Z]+[a-zA-Z0-9_]*$', name) or len(name) > 252:
        return 'No'
    
    if len([c for c in name if c.isdigit()]) > 3:
        return 'No'
    
    return 'Yes'
import unittest

class Test(unittest.TestCase):
    def test_valid_file_name(self):
        self.assertEqual(file_name_check("example.txt"), 'Yes')

    def test_invalid_file_name(self):
        self.assertEqual(file_name_check("1example.dll"), 'No')

    def test_invalid_file_name_too_many_digits(self):
        self.assertEqual(file_name_check("abc12345.txt"), 'No')

    def test_invalid_file_name_no_extension(self):
        self.assertEqual(file_name_check("filename"), 'No')

if __name__ == '__main__':
    unittest.main()