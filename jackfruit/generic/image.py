from typing import Mapping, Sequence

from telegram import Update, PhotoSize
from telegram.ext import CallbackContext

from generic import GenericView, GenericInputView


class ImageInputView(GenericInputView):
    def process_data(self, state: Mapping[str, 'GenericView'], update: 'Update', context: 'CallbackContext',
                     photo: Sequence[PhotoSize]) -> str:
        """Process user image input

        :param state: State dict
        :param update: Update object
        :param context: Callback context
        :param photo: User photo
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
        if update.message and update.message.photo:
            to_state = self.process_data(state, update, context, update.message.photo)
            state[to_state].show(update, context)
            return to_state
        return super().process(state, update, context)
