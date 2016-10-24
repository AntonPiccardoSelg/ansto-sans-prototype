import abc


class IValueConverter(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def convert(self, value):
        pass

    @abc.abstractmethod
    def convert_back(self, value):
        pass

    @staticmethod
    def create(convert, convert_back):
        class ValueConverter(IValueConverter):
            def convert(self, value):
                return convert(value)

            def convert_back(self, value):
                return convert_back(value)

        return ValueConverter()

    @staticmethod
    def default():
        class ValueConverter(IValueConverter):
            def convert(self, value):
                return value

            def convert_back(self, value):
                return value

        return ValueConverter()
