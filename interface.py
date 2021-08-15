from abc import ABCMeta, abstractmethod


class ISample(metaclass=ABCMeta):
    @abstractmethod
    def name(self):
        raise NotImplementedError()


class SampleLogic1(ISample):
    def name(self):
        print('This is SampleLogic1')


class SampleLogic2(ISample):
    def name(self):
        print('This is SampleLogic2')
