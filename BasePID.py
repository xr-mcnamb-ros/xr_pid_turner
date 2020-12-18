from abc import ABCMeta, abstractmethod


class AbstractPID(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def setPID(self, p: int, i: int, d: int) -> None:
        pass

    @abstractmethod
    def showPID(self):
        pass
