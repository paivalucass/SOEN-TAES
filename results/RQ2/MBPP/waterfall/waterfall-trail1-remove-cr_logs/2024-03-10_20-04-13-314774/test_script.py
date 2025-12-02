def extract_rear(test_tuple):
    rear_elements = []
    for string in test_tuple:
        if isinstance(string, str):
            if len(string) > 0:
                rear_elements.append(string[-1])
            else:
                rear_elements.append('')
        else:
            raise ValueError("Input tuple contains non-string elements")
    return rear_elements
import unittest

class Test(unittest.TestCase):
    def test_extract_rear(self):
        self.assertEqual(extract_rear(('Mers', 'for', 'Vers')), ['s', 'r', 's'])

if __name__ == '__main__':
    unittest.main()