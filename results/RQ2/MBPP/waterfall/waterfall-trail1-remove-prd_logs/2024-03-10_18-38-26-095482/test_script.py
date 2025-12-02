def remove_odd(str1):
    if not isinstance(str1, str):
        raise TypeError("Input must be a string")
    
    odd_indexed_chars = ''
    for i in range(len(str1)):
        if i % 2 != 0:
            odd_indexed_chars += str1[i]
    return odd_indexed_chars
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_odd('python'), 'yhn')

if __name__ == '__main__':
    unittest.main()