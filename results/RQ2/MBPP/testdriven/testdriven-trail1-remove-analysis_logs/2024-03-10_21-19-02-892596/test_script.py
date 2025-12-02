def extract_rear(test_tuple):
    '''
    Write a function to extract only the rear index element of each string in the given tuple.
    '''
    rear_elements = []
    for s in test_tuple:
        if isinstance(s, str) and s:
            rear_elements.append(s[-1])
        else:
            rear_elements.append('')
    return rear_elements
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_rear(('Mers', 'for', 'Vers')), ['s', 'r', 's'])

if __name__ == '__main__':
    unittest.main()