def count_occurance(s):
    count = 0
    index = 0
    while index < len(s):
        if s[index:index+3] == 'std':
            count += 1
            index += 3
        else:
            index += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_occurance("letstdlenstdporstd"), 3)

if __name__ == '__main__':
    unittest.main()