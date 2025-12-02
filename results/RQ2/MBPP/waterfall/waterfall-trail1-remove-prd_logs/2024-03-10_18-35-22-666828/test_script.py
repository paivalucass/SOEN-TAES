def colon_tuplex(tuplex, index, element):
    if index < 0 or index >= len(tuplex):
        return tuplex
    else:
        new_tuple = list(tuplex)
        if not isinstance(new_tuple[index], list):
            new_tuple[index] = [element]
        else:
            new_tuple[index].append(element)
        return tuple(new_tuple)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(colon_tuplex(("HELLO", 5, [], True), 2, 50), ("HELLO", 5, [50], True))

if __name__ == '__main__':
    unittest.main()