def removezero_ip(ip):
    # Split the IP address into its parts
    parts = ip.split('.')

    # Remove leading zeroes from each part
    modified_parts = [str(int(part)) for part in parts]

    # Join the modified parts back together
    modified_ip = '.'.join(modified_parts)

    # Return the modified IP address
    return modified_ip
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(removezero_ip("216.08.094.196"), '216.8.94.196')

if __name__ == '__main__':
    unittest.main()