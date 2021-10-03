from injector import Module
from interface import ISample, SampleLogic1, SampleLogic2


class SampleDIModule(Module):
    def configure(self, binder):
        # change here to SampleLogic2 if you needed
        binder.bind(ISample, to=SampleLogic1('foo'))
