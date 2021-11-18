from abc import ABCMeta
from abc import abstractmethod


class ISample(metaclass=ABCMeta):
    @abstractmethod
    def get_str(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    def name(self):
        raise NotImplementedError()

    @abstractmethod
    def show_param(self):
        raise NotImplementedError()


class SampleLogic1(ISample):
    def __init__(self, param: str):
        self.__param = param

    def get_str(self):
        return 'SampleLogic1'

    def name(self):
        print('This is SampleLogic1')

    def show_param(self):
        print('SampleLogic1 has a param with a value of {}'.format(self.__param))


class SampleLogic2(ISample):
    def get_str(self):
        return 'SampleLogic2'

    def name(self):
        print('This is SampleLogic2')

    def show_param(self):
        print('SampleLogic2 has a param with a value of {}'.format(self.__param))
