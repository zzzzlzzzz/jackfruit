from typing import Mapping, Any

from telegram import Update
from telegram.ext import CallbackContext


class GenericView:
    def get_name(self) -> str:
        """Return name of view (Class name by default)

        :return: View name
        """
        return self.__class__.__name__

    """Disable link preview for bot messages
    """
    disable_web_page_preview = None

    def get_disable_web_page_preview(self) -> bool:
        """Get disable_web_page_preview for bot messages

        :return: disable_web_page_preview
        """
        return self.disable_web_page_preview

    """Parse mode for bot messages
    """
    parse_mode = None

    def get_parse_mode(self) -> str:
        """Get parse_mode for show to user

        :return: parse_mode, see telegram.ParseMode
        """
        return self.parse_mode

    """Caption for show to user
    """
    text = None

    def get_text(self, update: 'Update', context: 'CallbackContext') -> str:
        """Get text for show to user

        :param update: Update object
        :param context: Context object
        :return: Text for show to user
        """
        return self.text

    def show(self, update: 'Update', context: 'CallbackContext', msg_id: int = None) -> None:
        """Show information for user

        :param update: Update object
        :param context: Callback context
        :param msg_id: Previous message id, if exists
        """
        pass

    def process(self, state: Mapping[str, 'GenericView'], update: 'Update', context: 'CallbackContext') -> str:
        """Process information received from user

        :param state: State dict
        :param update: Update object
        :param context: Callback context
        :return: New state
        """
        return self.get_name()


class GenericDataView(GenericView):
    """Using this view directly you can create read-view. User can move from this view only over commands.
    """
    def show(self, update: 'Update', context: 'CallbackContext', msg_id: int = None) -> None:
        """Show help text for user

        :param update: Update object
        :param context: Callback context
        :param msg_id: Previous message id, if exists
        """
        chat_id = update.effective_chat.id
        if msg_id:
            context.bot.edit_message_text(self.get_text(update, context), chat_id, msg_id,
                                          parse_mode=self.get_parse_mode(),
                                          disable_web_page_preview=self.get_disable_web_page_preview())
        else:
            context.bot.send_message(chat_id, self.get_text(update, context),
                                     parse_mode=self.get_parse_mode(),
                                     disable_web_page_preview=self.get_disable_web_page_preview())


class GenericDataInputView(GenericDataView):
    def get_user_input(self, update: 'Update') -> Any:
        """Return user input from update

        :param update: Update object
        :return: Target user data
        """
        return None

    def process_data(self, state: Mapping[str, 'GenericView'], update: 'Update', context: 'CallbackContext',
                     data: Any) -> str:
        """Process data contains in update received from user

        :param state: State dict
        :param update: Update object
        :param context: Callback context
        :param data: Data, received from user
        :return: New state
        """
        return self.get_name()

    def process(self, state: Mapping[str, 'GenericView'], update: 'Update', context: 'CallbackContext') -> str:
        """Process information received from user

        :param state: State dict
        :param update: Update object
        :param context: Callback context
        :return: New state
        """
        user_input = self.get_user_input(update)
        if user_input:
            to_state = self.process_data(state, update, context, user_input)
            state[to_state].show(update, context)
            return to_state
        return super().process(state, update, context)
