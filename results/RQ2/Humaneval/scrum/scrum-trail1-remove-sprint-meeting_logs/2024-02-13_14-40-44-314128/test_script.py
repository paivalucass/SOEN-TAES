def cycpattern_check(a, b):
    return b in (a + a) and len(a) == len(b)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test('abcd', 'abd'), False)
        self.assertEqual(function_under_test('hello', 'ell'), True)
        self.assertEqual(function_under_test('whassup', 'psus'), False)
        self.assertEqual(function_under_test('abab', 'baa'), True)
        self.assertEqual(function_under_test('efef', 'eeff'), False)
        self.assertEqual(function_under_test('himenss', 'simen'), True)

if __name__ == '__main__':
    unittest.main()