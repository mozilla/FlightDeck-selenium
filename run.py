import unittest
import sys

try:
    import settings_local as settings
except ImportError:
    try:
        import settings
    except ImportError:
        import sys
        sys.stderr.write(
            "Error: Tried importing 'settings_local.py' and 'settings.py' "
            "but neither could be found (or they're throwing an ImportError)."
            " Please come back and try again later.")
        raise

# identify test
# get tests

suite = unittest.TestSuite()

for arg in sys.argv[1:]:
    print "importing %s" % arg
    test_module = __import__('tests.%s' % arg)
    suite.addTest(unittest.defaultTestLoader.loadTestsFromModule(test_module))

runner = unittest.TextTestRunner()
runner.run(suite)
