from typing import Mapping

from telegram import Update
from telegram.ext import CallbackContext

from generic import GenericView, GenericInputView


class TextInputView(GenericInputView):
    def process_data(self, state: Mapping[str, 'GenericView'], update: 'Update', context: 'CallbackContext',
                     data: str) -> str:
        """Call for process user input

        :param state: State dict
        :param update: Update object
        :param context: Callback context
        :param data: User input
        :return: New state
        """
        return self.get_name()

    def process(self, state: Mapping[str, 'GenericView'], update: 'Update', context: 'CallbackContext') -> str:
        """Process user input

        :param state: State dict
        :param update: Update object
        :param context: Callback context
        :return: New state
        """
        if update.message and update.message.text:
            to_state = self.process_data(state, update, context, update.message.text)
            state[to_state].show(update, context)
            return to_state
        return super().process(state, update, context)
