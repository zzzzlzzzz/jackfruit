from typing import Mapping, Sequence, Tuple, Any

from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import CallbackContext

from generic import GenericView


class MenuView(GenericView):
    """List of menu item tuples
    [
        [
            (menu_item_text, menu_class_str),
            ...
        ],
        ...
    ]
    """
    menu_items = None

    def get_menu_items(self) -> Sequence[Sequence[Tuple[str, str]]]:
        """Get menu items for show to user

        :return: List of menu items tuples
        """
        return self.menu_items

    def process_data(self, state: Mapping[str, 'GenericView'], update: 'Update', context: 'CallbackContext',
                     data: str, msg_id: int = None) -> str:
        """Call if callback data not in states

        :param state: States array
        :param update: Update object
        :param context: Callback context
        :param data: Callback data
        :param msg_id: Previous message id, if exists
        :return: New state
        """
        return self.get_name()

    def get_inline_keyboard_button(self, text: str, data: str) -> 'InlineKeyboardButton':
        """Make InlineKeyboardButton from text and callback_data

        :param text: Text for button
        :param data: Callback data
        :return: Button
        """
        return InlineKeyboardButton(text, callback_data=data)

    def show(self, update: 'Update', context: 'CallbackContext', msg_id: int = None) -> None:
        """Show menu for user

        :param update: Update object
        :param context: Callback context
        :param msg_id: Previous message id, if exists
        """
        buttons = [[self.get_inline_keyboard_button(text, data) for text, data in row]
                   for row in self.get_menu_items()]
        markup = InlineKeyboardMarkup(buttons)
        chat_id = update.effective_chat.id
        if msg_id:
            context.bot.edit_message_text(self.get_text(), chat_id, msg_id,
                                          parse_mode=self.get_parse_mode(),
                                          disable_web_page_preview=self.get_disable_web_page_preview(),
                                          reply_markup=markup)
        else:
            context.bot.send_message(chat_id, self.get_text(),
                                     parse_mode=self.get_parse_mode(),
                                     disable_web_page_preview=self.get_disable_web_page_preview(),
                                     reply_markup=markup)

    def get_answer(self, data: str) -> Mapping[str, Any]:
        """Useful for adding message in answer to user

        :param data: Callback data
        """
        return dict()

    def process(self, state: Mapping[str, 'GenericView'], update: 'Update', context: 'CallbackContext') -> str:
        """Process user input

        :param state:`dict`: State dict
        :param update: Update object
        :param context: Callback context
        :return: New state
        """
        if update.callback_query:
            data = update.callback_query.data
            update.callback_query.answer(**self.get_answer(data))
            msg_id = update.callback_query.message.message_id
            if data in state:
                state[data].show(update, context, msg_id)
                return data
            else:
                return self.process_data(state, update, context, data, msg_id)
        return self.get_name()
