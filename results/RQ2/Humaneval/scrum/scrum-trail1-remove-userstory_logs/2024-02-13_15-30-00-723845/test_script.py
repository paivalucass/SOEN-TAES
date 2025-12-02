def Strongest_Extension(class_name, extensions):
    if not isinstance(class_name, str) or not isinstance(extensions, list):
        return "Invalid input"

    if not class_name or not extensions:
        return "Invalid input"

    strongest_extension = ""
    max_strength = float("-inf")

    for extension in extensions:
        uppercase_count = sum(1 for letter in extension if letter.isupper())
        lowercase_count = sum(1 for letter in extension if letter.islower())
        strength = uppercase_count - lowercase_count

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Strongest_Extension('my_class', ['AA', 'Be', 'CC']), 'my_class.AA')

if __name__ == '__main__':
    unittest.main()