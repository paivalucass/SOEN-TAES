import re

def removezero_ip(ip):
    if re.match(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', ip):
        ip_octets = ip.split('.')
        ip_without_zeroes = '.'.join(str(int(octet)) for octet in ip_octets)
        return ip_without_zeroes
    elif re.match(r'^([0-9a-fA-F]{1,4}:){7}([0-9a-fA-F]{1,4})$', ip):
        ip_blocks = ip.split(':')
        ip_blocks_without_zeroes = [block.lstrip('0') or '0' for block in ip_blocks]
        ip_without_zeroes = ':'.join(ip_blocks_without_zeroes)
        return ip_without_zeroes
    else:
        raise ValueError("Invalid input format")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(removezero_ip('216.08.094.196'), '216.8.94.196')

if __name__ == '__main__':
    unittest.main()