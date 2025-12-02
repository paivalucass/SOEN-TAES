def file_name_check(file_name):
    import re
    
    if len(re.findall(r'\d', file_name)) > 3:
        return 'No'
    if file_name.count('.') != 1:
        return 'No'
    
    name, ext = file_name.split('.')
    if len(name) == 0 or len(ext) == 0:
        return 'No'
    if not name[0].isalpha():
        return 'No'
    if ext not in ['txt', 'exe', 'dll']:
        return 'No'
    
    return 'Yes'
import unittest

class Test(unittest.TestCase):
    def test_valid_file_name(self):
        self.assertEqual(file_name_check("example.txt"), 'Yes')

    def test_invalid_file_name(self):
        self.assertEqual(file_name_check("1example.dll"), 'No')

if __name__ == '__main__':
    unittest.main()