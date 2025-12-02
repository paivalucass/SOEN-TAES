def is_happy(s):
    """
    You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    """

    # Check if the length of the string is less than 3
    if len(s) < 3:
        return False

    # Iterate through the string to check for consecutive 3 letters
    for i in range(len(s) - 2):
        if len(set(s[i:i+3])) < 3:
            return False

    return True
import unittest

class Test(unittest.TestCase):
    def test_is_happy(self):
        self.assertEqual(is_happy('a'), False)
        self.assertEqual(is_happy('aa'), False)
        self.assertEqual(is_happy('abcd'), True)
        self.assertEqual(is_happy('aabb'), False)
        self.assertEqual(is_happy('adb'), True)
        self.assertEqual(is_happy('xyy'), False)

if __name__ == '__main__':
    unittest.main()