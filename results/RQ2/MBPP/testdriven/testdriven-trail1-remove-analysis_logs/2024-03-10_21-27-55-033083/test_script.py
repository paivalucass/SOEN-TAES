def all_Characters_Same(s):
    '''Write a python function to check whether all the characters are same or not.'''
    if len(s) <= 1:
        return True
    return len(set(s)) == 1

# Test function
def test_all_Characters_Same():
    assert all_Characters_Same("") == True
    assert all_Characters_Same("a") == True
    assert all_Characters_Same("aaa") == True
    assert all_Characters_Same("abc") == False
    assert all_Characters_Same("aaaaaabbbccc") == False
    assert all_Characters_Same("python") == False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(all_Characters_Same('python'), False)

if __name__ == '__main__':
    unittest.main()