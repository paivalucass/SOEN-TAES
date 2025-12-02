def is_happy(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")

    if len(s) < 3:
        return False

    for i in range(len(s) - 2):
        if s[i] == s[i+1] or s[i] == s[i+2] or s[i+1] == s[i+2]:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_happy('a'), False)
        self.assertEqual(is_happy('aa'), False)
        self.assertEqual(is_happy('abcd'), True)
        self.assertEqual(is_happy('aabb'), False)
        self.assertEqual(is_happy('adb'), True)
        self.assertEqual(is_happy('xyy'), False)

if __name__ == '__main__':
    unittest.main()