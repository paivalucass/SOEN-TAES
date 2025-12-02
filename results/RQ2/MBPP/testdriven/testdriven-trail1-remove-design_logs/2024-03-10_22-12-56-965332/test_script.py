def removezero_ip(ip):
    '''Write a function to remove leading zeroes from an ip address.'''
    parts = list(map(int, ip.split('.')))
    new_parts = list(map(str, parts))
    return '.'.join(new_parts)

assert removezero_ip("216.08.094.196") == '216.8.94.196'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(removezero_ip("216.08.094.196"), '216.8.94.196')

if __name__ == '__main__':
    unittest.main()