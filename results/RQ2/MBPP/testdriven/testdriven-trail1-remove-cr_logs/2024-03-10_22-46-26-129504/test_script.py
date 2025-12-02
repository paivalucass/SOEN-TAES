import re

def removezero_ip(ip):
    ipv4_pattern = r'(\b\d{1,3}\b)\.?'
    ipv6_pattern = r'((?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?:(?::[0-9a-fA-F]{1,4}){1,6})|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)|::(?:(?::[0-9a-fA-F]{1,4}){1,7}|(?::[0-9a-fA-F]{1,4}){1,7}|(?::[0-9a-fA-F]{1,4}){1,7}|(?::[0-9a-fA-F]{1,4}){1,7}|(?::[0-9a-fA-F]{1,4}){1,7}|(?::[0-9a-fA-F]{1,4}){1,7}|(?::[0-9a-fA-F]{1,4}){1,7}|(?::[0-9a-fA-F]{1,4}){1,7})?)'
    if re.match(ipv4_pattern, ip):
        ip_segments = ip.split('.')
        ipv4_address = '.'.join(str(int(segment)) for segment in ip_segments)
        return ipv4_address
    elif re.match(ipv6_pattern, ip):
        # Implement IPv6 handling
        pass
    else:
        # Handle invalid IP address
        pass

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(removezero_ip('216.08.094.196'), '216.8.94.196')

if __name__ == '__main__':
    unittest.main()