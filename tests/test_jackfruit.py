from copy import deepcopy

from pytest import fixture

from jackfruit import *
from telegram.ext import CallbackQueryHandler, CommandHandler, MessageHandler, Filters, CallbackContext


@fixture()
def dispatcher():
    class DispatcherMock:
        HANDLERS = []

        def add_handler(self, h):
            self.HANDLERS.append(h)
    yield DispatcherMock()


@fixture()
def view():
    class GenericViewMock:
        def __init__(self):
            self.name = 'name'
            self.show_call = False

        def get_name(self):
            return self.name

        def process(self, state, update, context):
            return 'new_state'

        def show(self, update, context, msg_id=None):
            self.show_call = True
    yield GenericViewMock()


def test_single_view(dispatcher, view):
    j = Jackfruit(dispatcher, view)

    assert len(j.STATE) == 1
    assert j.STATE[view.get_name()] == view

    assert len(dispatcher.HANDLERS) == 2
    for h in dispatcher.HANDLERS:
        if isinstance(h, CallbackQueryHandler):
            assert h.callback == j._dispatch
        elif isinstance(h, MessageHandler):
            assert h.callback == j._dispatch
        else:
            assert False


def test_single_view_with_command(dispatcher, view):
    j = Jackfruit(dispatcher, view, [('start', view), ])

    assert len(dispatcher.HANDLERS) == 3
    for h in dispatcher.HANDLERS:
        if isinstance(h, CallbackQueryHandler):
            pass
        elif isinstance(h, MessageHandler):
            pass
        elif isinstance(h, CommandHandler):
            assert h.callback.func == j._dispatch_command
        else:
            assert False


def test_register_view(dispatcher, view):
    view2 = deepcopy(view)
    view2.name = 'name2'
    view3 = deepcopy(view)
    view3.name = 'name3'

    j = Jackfruit(dispatcher, view, [('start', view), ])
    j.register(view2, view3)

    assert len(j.STATE) == 3
    assert j.STATE[view.get_name()] == view
    assert j.STATE[view2.get_name()] == view2
    assert j.STATE[view3.get_name()] == view3


def test_dispatch(dispatcher, view, update, context):
    j = Jackfruit(dispatcher, view)
    j._dispatch(update, context)

    assert context.chat_data[j._state_key] == 'new_state'


def test_dispatch_command(dispatcher, view, update, context):
    j = Jackfruit(dispatcher, view)
    j._dispatch_command('name', update, context)

    assert context.chat_data[j._state_key] == 'name'
    assert view.show_call
