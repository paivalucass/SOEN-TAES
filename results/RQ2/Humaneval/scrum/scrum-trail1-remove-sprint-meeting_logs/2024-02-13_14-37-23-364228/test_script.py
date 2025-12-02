def cycpattern_check(a , b):
    temp = b + b
    return b in temp

import unittest

class Test(unittest.TestCase):
    def test_cycpattern_check(self):
        self.assertEqual(function_under_test('abcd','abd'), False)
        self.assertEqual(function_under_test('hello','ell'), True)
        self.assertEqual(function_under_test('whassup','psus'), False)
        self.assertEqual(function_under_test('abab','baa'), True)
        self.assertEqual(function_under_test('efef','eeff'), False)
        self.assertEqual(function_under_test('himenss','simen'), True)

if __name__ == '__main__':
    unittest.main()