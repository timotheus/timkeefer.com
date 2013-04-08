import types
import unittest

class TestGenExp(unittest.TestCase):
    def test_genexp(self):
        # Generator Expressions
        #
        # Create a generator expression ``to_five`` that generates
        # the numbers from 1 up to and including 5
        # ================================

        self.assertTrue(isinstance(to_five, types.GeneratorType))
        self.assertEqual(next(to_five), 1)
        self.assertEqual(list(to_five), [2,3,4,5])

        # Generator Expressions
        #
        # Write a function ``not_none`` that accepts a sequence
        # and uses a generator expression to generate the items
        # that aren't None
        # ================================

        self.assertTrue(isinstance(not_none(range(3)), types.GeneratorType))
        self.assertEqual(next(not_none([None, 1])), 1)
        self.assertRaises(StopIteration, next, not_none([None]))



if __name__ == '__main__':
    unittest.main()
