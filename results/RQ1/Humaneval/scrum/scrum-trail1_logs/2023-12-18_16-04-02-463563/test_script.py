def Strongest_Extension(class_name, extensions):
    import re

    def validate_input(class_name, extensions):
        if not isinstance(class_name, str) or not class_name:
            raise ValueError("Class name must be a non-empty string")
        
        if not all(isinstance(ext, str) for ext in extensions):
            raise ValueError("Extensions list must contain only strings")

    def calculate_strength(extension):
        cap_count = sum(1 for char in extension if char.isupper())
        sm_count = sum(1 for char in extension if char.islower())
        return cap_count - sm_count

    def find_strongest_extension(class_name, extensions):
        if not extensions:
            raise ValueError("Invalid input")

        strongest_extension = extensions[0]
        max_strength = calculate_strength(extensions[0])

        for extension in extensions[1:]:
            strength = calculate_strength(extension)
            if strength > max_strength:
                max_strength = strength
                strongest_extension = extension

        return f"{class_name}.{strongest_extension}"

    validate_input(class_name, extensions)
    return find_strongest_extension(class_name, extensions)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Strongest_Extension('my_class', ['AA', 'Be', 'CC']), 'my_class.AA')

if __name__ == '__main__':
    unittest.main()