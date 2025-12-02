def find_Rotations(input_str):
    if len(set(input_str)) == 1:
        return 1
    else:
        for i in range(1, len(input_str)):
            if input_str == input_str[i:] + input_str[:i]:
                return i
    return 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Rotations('aaaa'), 1)

if __name__ == '__main__':
    unittest.main()