try:
    from StringIO import StringIO
except ImportError as e:
    from io import StringIO
import sys
import types
import unittest

class TestDecorators(unittest.TestCase):
    def test_decorators(self):
        # Decorators
        #
        # create a decorator, ``noisy`` that
        # prints "before" before invoking the
        # wrapped function and "after", after
        # invoking it
        # ================================
        def noisy(func):

            def wrapper(*args, **kwargs):
                sys.stdout.write('before\n')
                result = func(*args, **kwargs)
                sys.stdout.write('after\n')
                return result

            return wrapper

        @noisy
        def nothing():
            sys.stdout.write('middle\n')

        old_stdout = sys.stdout
        sys.stdout = StringIO()
        nothing()
        captured = sys.stdout
        sys.stdout = old_stdout
        self.assertEqual(captured.getvalue(), 'before\nmiddle\nafter\n')
        self.assertTrue(isinstance(noisy, types.FunctionType))
        try:
            self.assertTrue(nothing.func_closure is not None)
        except AttributeError:
            self.assertTrue(nothing.__closure__ is not None)

        # Good decorators
        # write a decorator ``good_pointless`` that
        # updates the wrapped ``__doc__`` and ``__name__``
        # and just calls the function
        # ================================
        def good_pointless(func):

            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                return result

            wrapper.__doc__ = func.__doc__
            wrapper.__name__ = func.__name__
            return wrapper

        @good_pointless
        def nothing2():
            """doc string"""
            pass

        self.assertEqual(nothing2.__doc__, 'doc string')
        self.assertEqual(nothing2.__name__, 'nothing2')

        # Parameterized Decorators
        # write a decorator ``times_n`` that takes a
        # number (n) and multiples the result of the
        # function it is wrapping by that number (n).
        # ================================
        def times_n(mynum):
            def decorator(func):

                def wrapper(*args, **kwargs):
                    result = func(*args, **kwargs)
                    result = result * mynum
                    return result

                return wrapper
            return decorator

        @times_n(3)
        def echo(txt):
            return txt

        self.assertEqual(echo('f'), 'fff')
        self.assertEqual(echo(4), 12)



if __name__ == '__main__':
    unittest.main()
