def odd_Equivalent(binary_string, string_length):
    count = 0
    for i in range(len(binary_string)):
        if int(binary_string[i], 2) % 2 != 0:
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_Equivalent("011001", 6), 3)

if __name__ == '__main__':
    unittest.main()