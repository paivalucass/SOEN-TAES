def sort_sublists(input_list):
    return [sorted(sublist) for sublist in input_list]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_sublists([["green", "orange"], ["black", "white"], ["white", "black", "orange"]]), [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']])

if __name__ == '__main__':
    unittest.main()