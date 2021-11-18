from injector import Injector, inject

from interface import ISample
from di import SampleDIModule


class RequestSample:
    @inject
    def __init__(self, sample: ISample):
        self.__sample = sample

    def name(self):
        self.__sample.name()

    def show_param(self):
        self.__sample.show_param()


def main():
    injector = Injector([SampleDIModule('bar')])
    sample = injector.get(RequestSample)
    sample.name()
    sample.show_param()


if __name__ == '__main__':
    main()
