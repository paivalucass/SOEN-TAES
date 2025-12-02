def remove_odd(str1):
    new_string = ''.join([str1[i] for i in range(len(str1)) if i % 2 != 0])
    return new_string
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_odd('python'), 'yhn')

if __name__ == '__main__':
    unittest.main()