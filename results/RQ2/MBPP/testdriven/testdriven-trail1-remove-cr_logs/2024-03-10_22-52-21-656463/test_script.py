def number_ctr(s):
    import re
    if not isinstance(s, str) or not s:
        return 0
    else:
        count = len(re.findall(r'\d', s))
        return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(number_ctr('program2bedone'), 1)

if __name__ == '__main__':
    unittest.main()