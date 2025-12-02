def removezero_ip(ip):
    import re
    octets = ip.split('.')
    modified_octets = []
    for octet in octets:
        modified_octet = re.sub(r'^0+', '', octet)
        modified_octets.append(modified_octet)
    return '.'.join(modified_octets)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(removezero_ip('216.08.094.196'), '216.8.94.196')

if __name__ == '__main__':
    unittest.main()