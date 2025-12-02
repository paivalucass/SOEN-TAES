def count_occurance(s):
    if s is None:
        return 0
    if len(s) < 3:
        return 0

    count = 0
    for i in range(len(s)-2):
        if s[i:i+3] == 'std':
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_occurance('letstdlenstdporstd'), 3)

if __name__ == '__main__':
    unittest.main()