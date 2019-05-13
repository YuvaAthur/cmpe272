import unittest
import mongomock
import json


# Ref: https://gist.github.com/twolfson/13f5f5784f67fd49b245
class DBTestsBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """On inherited classes, run our `setUp` method"""
        # Inspired via http://stackoverflow.com/questions/1323455/python-unit-test-with-base-and-sub-class/17696807#17696807
        if cls is not DBTestsBase and cls.setUp is not DBTestsBase.setUp:
            orig_setUp = cls.setUp
            def setUpOverride(self, *args, **kwargs):
                DBTestsBase.setUp(self)
                return orig_setUp(self, *args, **kwargs)
            cls.setUp = setUpOverride

    def setUp(self):
        self.client = mongomock.MongoClient()

    def _steps(self):
        for name in dir(self): # dir() result is implicitly sorted
            if name.startswith("step"):
                yield name, getattr(self, name) 

    def test_steps(self):
        for name, step in self._steps():
            try:
                step()
            except Exception as e:
                self.fail("{} failed ({}: {})".format(step, type(e), e))

    def tearDown(self):
        pass
