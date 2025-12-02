import re

def file_name_check(file_name):
    pattern = re.compile(r"^[a-zA-Z][a-zA-Z0-9]{0,7}\.(txt|exe|dll)$")
    if pattern.match(file_name):
        return 'Yes'
    else:
        return 'No'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(file_name_check("example.txt"), 'Yes')
        self.assertEqual(file_name_check("1example.dll"), 'No')

if __name__ == '__main__':
    unittest.main()