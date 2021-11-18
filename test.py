import unittest

from injector import Injector

from di import TestDIModule
from main import RequestSample


class Test(unittest.TestCase):
    def test1(self):
        injector = Injector([TestDIModule()])
        sample = injector.get(RequestSample)

        self.assertEqual('SampleLogic2', sample.get_str())


if __name__ == '__main__':
    unittest.main()
