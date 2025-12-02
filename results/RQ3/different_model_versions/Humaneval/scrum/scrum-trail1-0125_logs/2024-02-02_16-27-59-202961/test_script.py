def file_name_check(file_name):
    if len([char for char in file_name if char.isdigit()]) > 3:
        return 'No'
    if file_name.count('.') != 1:
        return 'No'
    file_parts = file_name.split('.')
    if len(file_parts) != 2:
        return 'No'
    if not file_parts[0] or not file_parts[0][0].isalpha():
        return 'No'
    if file_parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(file_name_check("example.txt"), 'Yes')
        self.assertEqual(file_name_check("1example.dll"), 'No')
        self.assertEqual(file_name_check("file.with.multiple.dots.txt"), 'No')
        self.assertEqual(file_name_check("file.txt"), 'Yes')
        self.assertEqual(file_name_check("file.exe"), 'Yes')

if __name__ == '__main__':
    unittest.main()