def odd_values_string(s):
    return ''.join([s[i] for i in range(len(s)) if i % 2 == 0])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_values_string('abcdef'), 'ace')

if __name__ == '__main__':
    unittest.main()