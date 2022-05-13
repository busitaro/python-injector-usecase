import unittest

from injector import Injector

from di import TestDIModule
from main import RequestSample
from main import RequestSingleton


class Test(unittest.TestCase):
    def test1(self):
        injector = Injector([TestDIModule()])
        sample = injector.get(RequestSample)

        self.assertEqual('SampleLogic2', sample.get_str())

    def test2(self):
        injector = Injector([TestDIModule()])
        sample1 = injector.get(RequestSingleton)
        sample2 = injector.get(RequestSingleton)

        self.assertEqual(sample1.get_id(), sample2.get_id())


if __name__ == '__main__':
    unittest.main()
