def subject_marks(subject_marks):
    if not subject_marks:
        return "Input list is empty"
    for mark in subject_marks:
        if not isinstance(mark, tuple) or len(mark) != 2:
            return "Invalid data in input list"
    return sorted(subject_marks, key=lambda x: x[1])
import unittest

class TestSubjectMarks(unittest.TestCase):
    def test_subject_marks(self):
        self.assertEqual(subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]), [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)])

if __name__ == '__main__':
    unittest.main()