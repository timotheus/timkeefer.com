import types
import unittest

class SampleTest(unittest.TestCase):
    def test_example(self):
        """
        An example of how to do the tests
        """
        # Variables
        #
        # Create a variable ``name`` that is assigned to the string
        # "Matt".
        # ================================
        name = 'Matt'
        self.assertTrue(isinstance(name, str))
        self.assertEqual(name, 'Matt')

if __name__ == '__main__':
    unittest.main()
