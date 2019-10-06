from functools import partial
from typing import Tuple, Optional, Sequence

from telegram import Update
from telegram.ext import Dispatcher, CallbackQueryHandler, CommandHandler, MessageHandler, Filters, CallbackContext

from .generic import (GenericView, GenericDataInputView, MenuView, TextDataInputView, PhotoDataInputView,
                      AudioDataInputView, DocumentDataInputView)
from _version import __version__


__all__ = ['Jackfruit', 'GenericView', 'GenericDataInputView', 'MenuView', 'TextDataInputView', 'PhotoDataInputView',
           'AudioDataInputView', 'DocumentDataInputView', ]


class Jackfruit:
    STATE = dict()

    def __init__(self, dispatcher: 'Dispatcher', root_view: 'GenericView', commands: Sequence[Tuple[str, str]] = None):
        """Register handler in dispatcher

        :param dispatcher:  Dispatcher object
        :param root_view: Child class of GenericView
        :param commands: Standard /command list
        """
        self._state_key = self.__class__.__name__.upper()
        self._root_view = root_view.get_name()
        self.STATE[self._root_view] = root_view
        dispatcher.add_handler(CallbackQueryHandler(self._dispatch))
        dispatcher.add_handler(MessageHandler(~Filters.command, self._dispatch))
        if commands:
            for command, state in commands:
                dispatcher.add_handler(CommandHandler(command, partial(self._dispatch_command, state)))

    def register(self, state: 'GenericView', *args: Optional['GenericView']) -> None:
        """Register states in state registry

        :param state: View
        :param args: Any other views
        """
        for item in (state, *args):
            self.STATE[item.get_name()] = item

    def _dispatch(self, update: 'Update', context: 'CallbackContext') -> None:
        """Callback for dispatching updates to target class

        :param update: Update object
        :param context: Callback context
        """
        context.chat_data[self._state_key] = \
            self.STATE[context.chat_data.setdefault(self._state_key, self._root_view)]. \
                process(self.STATE, update, context)

    def _dispatch_command(self, state: str, update: 'Update', context: 'CallbackContext') -> None:
        """Callback for dispatching updates for fast commands

        :param state: State to move
        :param update: Update object
        :param context: Callback context
        """
        context.chat_data[self._state_key] = state
        self.STATE[state].show(update, context)
