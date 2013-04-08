import types
import unittest

class TestClosures(unittest.TestCase):
    def test_closure(self):
        # Closure
        #
        # Create a function ``echo_creator`` that returns a function that returns what was passed into it
        # ================================
        def echo_creator():
            def myfunc(x):
                return x

            return myfunc

        echo = echo_creator()
        self.assertTrue(isinstance(echo, types.FunctionType))
        self.assertEqual(echo(5), 5)
        self.assertEqual(echo("foo"), "foo")

        # Closure 2
        # Create a function ``mult_factory`` that accepts
        # a number and returns a function that multiples its
        # input by that number
        # ================================
        def mult_factory(mynum):
            def multi(x):
                return mynum * x

            return multi

        mult5 = mult_factory(5)
        self.assertTrue(isinstance(mult5, types.FunctionType))
        self.assertEqual(mult5(5), 25)
        self.assertEqual(mult5("f"), "fffff")


if __name__ == '__main__':
    unittest.main()
