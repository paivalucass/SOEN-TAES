def cycpattern_check(a, b):
    for i in range(len(b)):
        if b in a:
            return True
        b = b[1:] + b[0]
    return False
import unittest

class Test(unittest.TestCase):
    def test_cycpattern_check(self):
        self.assertEqual(function_under_test('abcd', 'abd'), False)
        self.assertEqual(function_under_test('hello', 'ell'), True)
        self.assertEqual(function_under_test('whassup', 'psus'), False)
        self.assertEqual(function_under_test('abab', 'baa'), True)
        self.assertEqual(function_under_test('efef', 'eeff'), False)
        self.assertEqual(function_under_test('himenss', 'simen'), True)

if __name__ == '__main__':
    unittest.main()