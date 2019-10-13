# Jackfruit
## Introduction
This library provides a simple way for creating telegram bots with deep level menu.
## Components
Library give users components, like:

* Menu (_MenuView_) - give user ability select menu item and navigate on menus;
* Text Input (_TextDataInputView_) - give user ability enter text data;
* Image Input (_PhotoDataInputView_) - give user ability send image to bot;
* Document Input (_DocumentDataInputView_) - give user ability send files to bot;
* Audio Input (_AudioDataInputView_) - give user ability send audio files to bot;
* Video Input (_VideoDataInputView_) - give user ability send video files to bot;
* Voice Input (_VoiceDataInputView_) - give user ability send voice messages to bot;
* Sticker Input (_StickerDataInputView_) - give user ability send sticker to bot;

You can use class _GenericDataView_ for show user screen, that blocking next navigation and force user to use command syntax.

All components may be easy customized, for more details please see source code (it have commented).
## Usage
```python
from os import environ

from telegram.ext import Updater

from jackfruit import *


class MainMenu(MenuView):
    text = 'Hello from my bot!'
    menu_items = [[('Enter my name', 'EnterName'), ('Select my age', 'SelectAge')], ]


class EnterName(TextDataInputView):
    text = 'Enter my name:'

    def process_data(self, state, update, context, data):
        return 'MainMenu'


class SelectAge(MenuView):
    text = 'Select my age:'
    menu_items = [[('Below 18', 'MainMenu'), ('Above 18', 'MainMenu')]]


updater = Updater(environ['TOKEN'], use_context=True)
main_menu = MainMenu()
enter_name = EnterName()
select_age = SelectAge()
Jackfruit(updater.dispatcher, main_menu, [('start', 'MainMenu')]).register(enter_name, select_age)
updater.start_polling()
updater.idle()
```