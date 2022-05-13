from injector import Module
from injector import singleton
from injector import provider

from interface import ISample
from interface import SampleLogic1
from interface import SampleLogic2
from interface import ISingletonSample
from interface import SingletonSample


class SampleDIModule(Module):
    def __init__(self, param: str):
        self.__param = param

    def configure(self, binder):
        # change here to SampleLogic2 if you needed
        binder.bind(ISample, to=SampleLogic1(self.__param))


class TestDIModule(Module):
    def configure(self, binder):
        # binder for unittest
        binder.bind(ISample, to=SampleLogic2())

    @singleton
    @provider
    def provide_sample(self) -> ISingletonSample:
        return SingletonSample()


class SingletonDIModule(Module):
    @singleton
    @provider
    def provide_sample(self) -> ISingletonSample:
        return SingletonSample()
