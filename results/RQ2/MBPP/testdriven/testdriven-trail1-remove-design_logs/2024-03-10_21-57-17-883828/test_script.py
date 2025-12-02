def find_substring(str1, sub_str):
    for s in str1:
        if s.find(sub_str) != -1:
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_substring(["red", "black", "white", "green", "orange"],"ack"), True)

if __name__ == '__main__':
    unittest.main()