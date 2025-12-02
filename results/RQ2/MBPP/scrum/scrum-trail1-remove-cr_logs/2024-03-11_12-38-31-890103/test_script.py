def index_minimum(test_list):
    if not test_list:
        return None
    
    try:
        test_list.sort(key=lambda x: x[1])
        return test_list[0][0]
    except (IndexError, ValueError, TypeError):
        return "ValueError"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]), 'Varsha')

if __name__ == '__main__':
    unittest.main()