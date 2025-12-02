def is_undulating(n):
    '''Write a function to check whether the given number is undulating or not.
    assert is_undulating(1212121) == True'''

    if len(str(n)) < 3:
        return False
    
    num_str = str(n)
    
    for i in range(1, len(num_str) - 1):
        if (num_str[i - 1] < num_str[i] > num_str[i + 1]) or (num_str[i - 1] > num_str[i] < num_str[i + 1]):
            continue
        else:
            return False
    
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_undulating(1212121), True)

if __name__ == '__main__':
    unittest.main()