def removezero_ip(ip):
    '''Write a function to remove leading zeroes from an ip address.'''
    if not isinstance(ip, str):
        return "Invalid input"

    octets = ip.split('.')
    if len(octets) != 4:
        return "Invalid IP address"

    for octet in octets:
        if not octet.isdigit() or not 0 <= int(octet) <= 255:
            return "Invalid IP address"

    modified_octets = []
    for octet in octets:
        modified_octets.append(str(int(octet)))

    return '.'.join(modified_octets)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(removezero_ip("216.08.094.196"), '216.8.94.196')

if __name__ == '__main__':
    unittest.main()