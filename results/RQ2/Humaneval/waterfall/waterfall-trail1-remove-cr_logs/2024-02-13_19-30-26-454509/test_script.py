def Strongest_Extension(class_name, extensions):
    if not class_name or not extensions or not all(isinstance(ext, str) for ext in extensions):
        raise ValueError("Invalid input format")

    strongest_extension = ''
    strongest_strength = float('-inf')

    for extension in extensions:
        cap_count = sum(1 for letter in extension if letter.isupper())
        sm_count = sum(1 for letter in extension if letter.islower())
        strength = cap_count - sm_count

        if strength > strongest_strength:
            strongest_extension = extension
            strongest_strength = strength

    return f'{class_name}.{strongest_extension}'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Strongest_Extension('my_class', ['AA', 'Be', 'CC']), 'my_class.AA')

if __name__ == '__main__':
    unittest.main()