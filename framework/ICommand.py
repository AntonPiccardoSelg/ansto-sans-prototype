import abc


class ICommand(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def can_execute(self):
        pass

    @abc.abstractmethod
    def execute(self):
        pass
