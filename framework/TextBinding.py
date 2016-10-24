from BindingMode import BindingMode
from IBinding import IBinding
from IPropertyListener import IPropertyListener
from IValueConverter import IValueConverter


class TextBinding(IBinding):

    class SourceListener(IPropertyListener):
        def __init__(self, property, target, converter):
            super(TextBinding.SourceListener, self).__init__()

            self._property = property
            self._target = target
            self._converter = converter

        def on_property_changed(self, model, property, value):
            if property == self._property:
                TextBinding.convert_to_target(value, self._target, self._converter, force=False)

    def __init__(self, property_info, target, mode=BindingMode.TwoWay, converter=IValueConverter.default()):
        super(TextBinding, self).__init__()

        if mode is BindingMode.TwoWay or mode is BindingMode.OneWay:
            self._property_info = property_info
            self._property_info_listener = TextBinding.SourceListener(property_info.name, target, converter)
            self._property_info.add_listener(self._property_info_listener)
            self.convert_to_target(property_info.get_value(), target, converter, force=True)
        else:
            self._source_listener = None

        if mode is BindingMode.TwoWay or mode is BindingMode.OneWayToSource:
            self._target = target
            self._target_edited = lambda text: self.convert_to_model(target, text, property_info, converter)
            self._target_finished = lambda: self.convert_to_target(property_info.get_value(), target, converter, force=True)
            self._target.textEdited.connect(self._target_edited)
            self._target.editingFinished.connect(self._target_finished)
        else:
            self._target_slot = None

    def destroy(self):
        try:
            if self._property_info_listener:
                self._property_info.remove_listener(self._property_info_listener)
                self._property_info_listener = None
        finally:
            try:
                if self._target_edited:
                    self._target.textEdited.disconnect(self._target_edited)
                    self._target_edited = None
            finally:
                if self._target_finished:
                    self._target.editingFinished.disconnect(self._target_finished)
                    self._target_finished = None

    @staticmethod
    def convert_to_model(target, text, property_info, converter):
        try:
            property_info.set_value(converter.convert_back(str(text)))
            target.setStyleSheet("")
        except:
            try:
                target.setStyleSheet("background-color:pink;")
            except:
                pass

    @staticmethod
    def convert_to_target(value, target, converter, force=False):
        if force:
            try:
                target.setText(converter.convert(value))
                target.setStyleSheet("")
            except:
                target.setStyleSheet("background-color:pink;")
        else:
            try:
                if converter.convert_back(str(target.text())) != value:
                    TextBinding.convert_to_target(value, target, converter, force=True)
            except:
                TextBinding.convert_to_target(value, target, converter, force=True)
