def count_occurance(s):
    import re
    if s:
        return len(re.findall('std', s))
    else:
        return 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_occurance("letstdlenstdporstd"), 3)

if __name__ == '__main__':
    unittest.main()