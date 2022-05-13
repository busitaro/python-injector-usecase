from injector import Injector
from injector import inject

from interface import ISample
from interface import ISingletonSample
from di import SampleDIModule
from di import SingletonDIModule


class RequestSample:
    @inject
    def __init__(self, sample: ISample):
        self.__sample = sample

    def get_str(self):
        return self.__sample.get_str()

    def name(self):
        self.__sample.name()

    def show_param(self):
        self.__sample.show_param()


class RequestSingleton:
    @inject
    def __init__(self, sample: ISingletonSample):
        self.__sample = sample

    def get_id(self):
        return self.__sample.get_id

    def show_id(self):
        return self.__sample.show_id()


def main():
    print('------ DI with parameter ------')
    # DI with parameter
    injector = Injector([SampleDIModule('bar')])
    sample = injector.get(RequestSample)
    sample.name()
    sample.show_param()

    print('------ DI with singleton ------')
    # DI by singleton
    injector = Injector([SingletonDIModule()])
    sample1 = injector.get(RequestSingleton)
    sample2 = injector.get(RequestSingleton)
    sample1.show_id()
    sample2.show_id()


if __name__ == '__main__':
    main()
