def is_sublist(l, s):
    if not isinstance(l, list) or not isinstance(s, list):
        raise ValueError("Both parameters should be lists")

    if len(s) == 0 or len(s) > len(l):
        raise ValueError("Sublist should not be empty or longer than the main list")

    for i in range(len(l)):
        if l[i] == s[0]:
            if l[i:i + len(s)] == s:
                return True

    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_sublist([2,4,3,5,7],[3,7]), False)

if __name__ == '__main__':
    unittest.main()