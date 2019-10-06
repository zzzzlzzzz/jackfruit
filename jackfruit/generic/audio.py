from typing import Any

from telegram import Update

from .generic import GenericDataInputView


class AudioDataInputView(GenericDataInputView):
    def get_user_input(self, update: 'Update') -> Any:
        """Return user input from update

        :param update: Update object
        :return: Target user data
        """
        try:
            return update.message.audio
        except AttributeError:
            return None
