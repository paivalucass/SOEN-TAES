def removezero_ip(ip):
    octets = ip.split('.')
    if len(octets) != 4:
        return "Invalid IP address format"
    for octet in octets:
        if not octet.isdigit() or int(octet) < 0 or int(octet) > 255:
            return "Invalid IP address range"
    modified_octets = [str(int(octet)) for octet in octets]  
    modified_ip = '.'.join(modified_octets)  
    return modified_ip
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(removezero_ip('216.08.094.196'), '216.8.94.196')

if __name__ == '__main__':
    unittest.main()