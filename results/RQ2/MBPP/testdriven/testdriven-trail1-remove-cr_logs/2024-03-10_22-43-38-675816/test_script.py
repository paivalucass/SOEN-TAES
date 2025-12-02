def check_Consecutive(l): 
    # Implementation details
    # Checking for empty list
    if not l:
        return False
    # Sorting the list
    l.sort()
    # Checking for consecutive numbers
    for i in range(len(l)-1):
        if l[i] + 1 != l[i+1]:
            return False
    return True

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_Consecutive([1,2,3,4,5]), True)

if __name__ == '__main__':
    unittest.main()