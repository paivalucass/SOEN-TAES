def removezero_ip(ip):
    ip_sections = ip.split('.')
    modified_ip = []
    for section in ip_sections:
        try:
            modified_ip.append(str(int(section)))
        except ValueError:
            return "Invalid IP Address"
    return '.'.join(modified_ip)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(removezero_ip('216.08.094.196'), '216.8.94.196')

if __name__ == '__main__':
    unittest.main()