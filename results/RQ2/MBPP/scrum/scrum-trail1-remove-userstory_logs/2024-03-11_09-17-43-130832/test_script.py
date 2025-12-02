def removezero_ip(ip):
    if not ip:
        return "Invalid IP address"

    segments = ip.split('.')

    if len(segments) != 4:
        return "Invalid IP address"

    for segment in segments:
        if not segment.isdigit() or not 0 <= int(segment) <= 255:
            return "Invalid IP address"

    modified_segments = [str(int(segment)) for segment in segments]

    modified_ip = '.'.join(modified_segments)

    return modified_ip
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(removezero_ip('216.08.094.196'), '216.8.94.196')

if __name__ == '__main__':
    unittest.main()