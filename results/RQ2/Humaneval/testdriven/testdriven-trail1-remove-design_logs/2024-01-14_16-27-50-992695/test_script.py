def file_name_check(file_name):
    if len([char for char in file_name if char.isdigit()]) > 3:
        return 'No'
    if file_name.count('.') != 1:
        return 'No'
    file_name_split = file_name.split('.')
    if not file_name_split[0]:
        return 'No'
    if not file_name_split[0][0].isalpha():
        return 'No'
    if file_name_split[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
import unittest

class Test(unittest.TestCase):
    def test_valid_file_name(self):
        self.assertEqual(file_name_check('example.txt'), 'Yes')

    def test_invalid_file_name(self):
        self.assertEqual(file_name_check('1example.dll'), 'No')

if __name__ == '__main__':
    unittest.main()