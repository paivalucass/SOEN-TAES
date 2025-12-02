def find_dissimilar(test_tup1, test_tup2):
    dissimilar_elements = []
    for element in test_tup1:
        if element not in test_tup2:
            dissimilar_elements.append(element)
    for element in test_tup2:
        if element not in test_tup1:
            dissimilar_elements.append(element)
    return tuple(dissimilar_elements)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)), (3, 6, 7, 10))

if __name__ == '__main__':
    unittest.main()