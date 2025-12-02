def is_happy(s):
    if len(s) < 3:
        return False
    
    def check_distinct(chunk):
        return len(set(chunk)) == 3
    
    for i in range(0, len(s) - 2):
        if not check_distinct(s[i:i+3]):
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