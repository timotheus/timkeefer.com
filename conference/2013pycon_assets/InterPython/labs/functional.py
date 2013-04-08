import types
import unittest

class TestFunctional(unittest.TestCase):
    def test_functional(self):
        # Lambda
        # create a lambda statement that adds 2 to its input
        # assign the statement to a variable named ``add_2``
        # ================================
        add_2 = lambda a: a + 2

        self.assertTrue(isinstance(add_2, types.LambdaType))
        self.assertEqual(add_2(4), 6)

        # Lamda 2
        # Create an ``is_odd`` lambda statement,
        # that evaluates to True if the input is odd
        # ================================
        is_odd = lambda a: False if a %2 == 0 else True
        self.assertTrue(isinstance(is_odd, types.LambdaType))
        self.assertEqual(is_odd(5), True)
        self.assertEqual(is_odd(4), False)


        # Map
        # Create a list ``digits`` with the numbers from 0 to 9
        # Create a new list ``two_more`` from digits by
        # mapping ``add_2`` to the elements of digits
        # ================================
        digits = range(10)
        self.assertEqual(digits, list(range(0, 10)))
        self.assertEqual(two_more, list(range(2,12)))

        # Reduce
        # Add the values of ``digits`` by using
        # ``reduce`` with the ``operator.add``
        # function, store the result in ``digit_sum``
        # ================================

        self.assertEqual(digit_sum, 45)

        # Filter
        # use ``filter`` to get the odd digits of the
        # ``two_more`` list, store results in ``two_odd``.
        # (hint use ``is_odd`` as the predicate function)
        # ================================

        self.assertEqual(list(two_odd), [3, 5, 7, 9, 11])



if __name__ == '__main__':
    unittest.main()
