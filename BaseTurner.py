from abc import ABCMeta, abstractmethod


class AbstractTurner(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def stop(self):
        pass

