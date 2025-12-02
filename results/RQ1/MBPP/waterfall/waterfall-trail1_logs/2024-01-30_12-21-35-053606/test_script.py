def subject_marks(tuple_list):
    if not isinstance(tuple_list, list):
        raise TypeError("Input must be a list")
    if not all(isinstance(t, tuple) and len(t) >= 2 for t in tuple_list):
        raise ValueError("Input must be a list of tuples with at least two elements")

    return sorted(tuple_list, key=lambda x: x[1])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]), [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)])

if __name__ == '__main__':
    unittest.main()