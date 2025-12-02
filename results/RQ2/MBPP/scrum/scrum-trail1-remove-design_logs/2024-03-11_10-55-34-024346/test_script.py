def removezero_ip(ip):
    parts = ip.split(".")
    new_parts = []
    for part in parts:
        new_parts.append(str(int(part)))
    return ".".join(new_parts)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(removezero_ip("216.08.094.196"), '216.8.94.196')

if __name__ == '__main__':
    unittest.main()