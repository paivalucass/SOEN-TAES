def file_name_check(file_name):
    if not isinstance(file_name, str) or not file_name:
        return 'No'
    if file_name.count('.') != 1:
        return 'No'
    name, extension = file_name.split('.')
    if not name or not name[0].isalpha():
        return 'No'
    if len([c for c in name if c.isdigit()]) > 3:
        return 'No'
    if extension not in ['txt', 'exe', 'dll']:
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