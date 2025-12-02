def check_consecutive(l):
    if len(l) < 2:
        return False
    
    l.sort()
    for i in range(len(l) - 1):
        if l[i] + 1 != l[i + 1]:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_Consecutive([1,2,3,4,5]), True)

if __name__ == '__main__':
    unittest.main()