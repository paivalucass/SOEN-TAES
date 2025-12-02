def extract_quotation(text):
    import re
    if not isinstance(text, str):
        raise ValueError("Input text must be a valid string")

    extracted_values = re.findall(r'\"(.*?)\"', text)

    return extracted_values
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_quotation('Cortex "A53" Based "multi" tasking "Processor"'), ['A53', 'multi', 'Processor'])

if __name__ == '__main__':
    unittest.main()