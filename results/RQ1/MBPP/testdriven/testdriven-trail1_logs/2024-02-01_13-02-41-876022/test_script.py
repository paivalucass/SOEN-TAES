def removezero_ip(ip):
    import re
    pattern = r'(?<!\d)0+(\d)'
    cleaned_ip = re.sub(pattern, r'\1', ip)
    return cleaned_ip

assert removezero_ip("216.08.094.196") == "216.8.94.196"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(removezero_ip('216.08.094.196'), '216.8.94.196')

if __name__ == '__main__':
    unittest.main()