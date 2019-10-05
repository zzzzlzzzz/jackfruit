# Jackfruit
## Introduction
This library provides a simple way for creating telegram bots with deep level menu.
## Usage
```python
from os import environ

from telegram.ext import Updater

from jackfruit import *


class MainMenu(MenuView):
    text = 'Hello from my bot!'
    menu_items = [[('Enter my name', 'EnterName'), ('Select my age', 'SelectAge')], ]


class EnterName(TextInputView):
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