def upper_ctr(s):
    import re
    pattern = re.compile(r'[A-Z]')
    return len(pattern.findall(s))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(upper_ctr('PYthon'), 2)

if __name__ == '__main__':
    unittest.main()