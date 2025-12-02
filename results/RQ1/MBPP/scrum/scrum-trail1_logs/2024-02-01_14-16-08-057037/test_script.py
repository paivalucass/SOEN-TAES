def subject_marks(subjectmarks):
    if len(subjectmarks) <= 1:
        return subjectmarks
    
    mid = len(subjectmarks) // 2
    left = subjectmarks[:mid]
    right = subjectmarks[mid:]

    left = subject_marks(left)
    right = subject_marks(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i][1] <= right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result += left[i:]
    result += right[j:]
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]), [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)])

if __name__ == '__main__':
    unittest.main()