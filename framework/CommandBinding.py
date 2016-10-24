from PyQt4.QtCore import QTimer
from ICommand import ICommand
from IPropertyListener import IPropertyListener
from ViewModel import ViewModel


class CommandBinding(object):

    class GlobalListener(IPropertyListener):
        def __init__(self, callback):
            super(CommandBinding.GlobalListener, self).__init__()

            self._triggered = True
            self._callback = callback
            self._callback()

        def on_property_changed(self, model, property, value):
            if not self._triggered:
                self._triggered = True
                self._callback()

        def reset(self):
            self._triggered = False

    def __init__(self, command, target):
        super(CommandBinding, self).__init__()

        if not isinstance(command, ICommand):
            raise ValueError("CommandBinding: the specified command is not of type \"ICommand\"")

        self._command = command
        self._target = target
        self._target_slot = lambda: command.execute() if command.can_execute else None

        self._target.setEnabled(False)
        self._target.clicked.connect(self._target_slot)

        self._listener = CommandBinding.GlobalListener(lambda: QTimer.singleShot(0, self.update))
        ViewModel.add_global_listener(self._listener)

    def destroy(self):
        try:
            if self._target_slot:
                self._target.clicked.disconnect(self._target_slot)
                self._target_slot = None
        finally:
            if self._listener:
                ViewModel.remove_global_listener(self._listener)
                self._listener = None

    def update(self):
        can_execute = self._command.can_execute
        if self._target.isEnabled() != can_execute:
            self._target.setEnabled(can_execute)

        if self._listener:
            self._listener.reset()
