def file_name_check(file_name):
    if file_name.count('.') != 1:
        return 'No'
    name, ext = file_name.split('.')
    if len(name) == 0 or not name[0].isalpha():
        return 'No'
    if ext not in ['txt', 'exe', 'dll']:
        return 'No'
    if sum(c.isdigit() for c in name) > 3:
        return 'No'
    return 'Yes'
import unittest

class Test(unittest.TestCase):
    def test_file_name_check(self):
        self.assertEqual(file_name_check('example.txt'), 'Yes')
        self.assertEqual(file_name_check('1example.dll'), 'No')

if __name__ == '__main__':
    unittest.main()