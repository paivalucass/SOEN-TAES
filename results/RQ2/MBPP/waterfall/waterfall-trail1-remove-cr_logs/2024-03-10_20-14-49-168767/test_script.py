def extract_quotation(text1):
    # Write a function to extract values between quotation marks " " of the given string
    import re
    return re.findall(r'"(.*?)"', text1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_quotation('Cortex "A53" Based "multi" tasking "Processor"'), ['A53', 'multi', 'Processor'])

if __name__ == '__main__':
    unittest.main()