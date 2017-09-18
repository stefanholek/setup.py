import unittest


class TestMyPackage(unittest.TestCase):

    def test_installation(self):
        import mypackage

    def test_main(self):
        from mypackage.mypackage import main
