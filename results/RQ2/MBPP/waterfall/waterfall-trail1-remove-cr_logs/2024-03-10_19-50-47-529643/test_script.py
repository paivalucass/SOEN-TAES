from typing import List, Tuple

def subject_marks(tuples: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    tuples.sort(key=lambda x: x[1])
    return tuples
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]), [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)])

if __name__ == '__main__':
    unittest.main()