def check_Consecutive(l): 
    for i in range(len(l)-1):
        if not isinstance(l[i], int) or not isinstance(l[i+1], int):
            return "Error"
        if l[i] + 1 != l[i+1]:
            return False
    return True

assert check_Consecutive([1,2,3,4,5]) == True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_Consecutive([1,2,3,4,5]), True)

if __name__ == '__main__':
    unittest.main()