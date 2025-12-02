def find_Rotations(str):
    count = 1
    for i in range(1, len(str)):
        if str[i] != str[0]:
            count += 1
    return count

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Rotations('aaaa'), 1)

if __name__ == '__main__':
    unittest.main()