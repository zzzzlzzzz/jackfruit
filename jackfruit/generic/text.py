from typing import Mapping

from telegram import Update
from telegram.ext import CallbackContext

from generic import GenericView


class TextInputView(GenericView):
    def process_data(self, state: Mapping[str, 'GenericView'], update: 'Update', context: 'CallbackContext',
                     data: str) -> str:
        """Call for process user input

        :param state: States array
        :param update: Update object
        :param context: Callback context
        :param data: User input
        :return: New state
        """
        return self.get_name()

    def show(self, update: 'Update', context: 'CallbackContext', msg_id: int = None) -> None:
        """Show text input for user

        :param update: Update object
        :param context: Callback context
        :param msg_id: Previous message id, if exists
        """
        chat_id = update.effective_chat.id
        if msg_id:
            context.bot.edit_message_text(self.get_text(), chat_id, msg_id,
                                          parse_mode=self.get_parse_mode(),
                                          disable_web_page_preview=self.get_disable_web_page_preview())
        else:
            context.bot.send_message(chat_id, self.get_text(),
                                     parse_mode=self.get_parse_mode(),
                                     disable_web_page_preview=self.get_disable_web_page_preview())

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
        return self.get_name()
