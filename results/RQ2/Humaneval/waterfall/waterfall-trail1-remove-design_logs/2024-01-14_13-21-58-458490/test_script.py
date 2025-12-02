def Strongest_Extension(class_name, extensions):
    strengths = {}
    for ext in extensions:
        uppercase_count = sum(1 for c in ext if c.isupper())
        lowercase_count = sum(1 for c in ext if c.islower())
        strengths[ext] = uppercase_count - lowercase_count
    strongest_extension = max(strengths, key=strengths.get)
    return f"{class_name}.{strongest_extension}"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Strongest_Extension('my_class', ['AA', 'Be', 'CC']), 'my_class.AA')

if __name__ == '__main__':
    unittest.main()