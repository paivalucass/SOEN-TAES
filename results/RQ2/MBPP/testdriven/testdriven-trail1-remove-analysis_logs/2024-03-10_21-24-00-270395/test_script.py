def removezero_ip(ip):
    '''Write a function to remove leading zeroes from an ip address.
    assert removezero_ip("216.08.094.196")==('216.8.94.196')'''
    import re
    if not ip:
        return 'Invalid input'
    
    pattern = r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    if not re.match(pattern, ip):
        return 'Invalid input'
    
    octets = ip.split('.')
    for i in range(4):
        octets[i] = str(int(octets[i]))
    
    return '.'.join(octets)
import unittest

class Test(unittest.TestCase):
    def test_removezero_ip(self):
        self.assertEqual(removezero_ip('216.08.094.196'), '216.8.94.196')

if __name__ == '__main__':
    unittest.main()