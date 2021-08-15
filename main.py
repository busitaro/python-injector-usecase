from injector import Injector, inject

from interface import ISample
from di import SampleDIModule


class RequestSample:
    @inject
    def __init__(self, sample: ISample):
        self.__sample = sample

    def name(self):
        self.__sample.name()


def main():
    injector = Injector([SampleDIModule()])
    sample = injector.get(RequestSample)
    sample.name()


if __name__ == '__main__':
    main()
