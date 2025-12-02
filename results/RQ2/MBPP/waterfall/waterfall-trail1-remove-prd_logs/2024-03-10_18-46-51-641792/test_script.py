def all_Characters_Same(s):
    if not isinstance(s, str):
        return False
    
    if len(s) == 0:
        return False
    
    return all(char == s[0] for char in s)

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(all_Characters_Same("python"), False)

if __name__ == '__main__':
    unittest.main()