def remove_odd(str1):
    new_str = ''
    if type(str1) is not str:
        return 'Error: Input is not a string'
    if str1 is None:
        return 'Error: Input is null'
    for i in range(len(str1)):
        if i % 2 != 0:
            new_str += str1[i]
    return new_str
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_odd('python'), 'yhn')

if __name__ == '__main__':
    unittest.main()