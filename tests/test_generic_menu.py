from copy import deepcopy

from pytest import fixture

from jackfruit import MenuView


@fixture()
def view():
    class MenuViewMock(MenuView):
        menu_items = [[('Menu 1', 'menu1'), ('Menu 2', 'menu2')], [('Menu 3', 'menu3')]]
    yield MenuViewMock()


def test_get_menu_items(view, update, context):
    assert view.get_menu_items(update, context) == view.menu_items


def test_process_data(view, update, context):
    assert view.process_data(dict(), update, context, 'data') == view.get_name()


def test_get_inline_keyboard_button(view):
    button = view.get_inline_keyboard_button('Menu X', 'menux')
    assert button.text == 'Menu X'
    assert button.callback_data == 'menux'


def test_show(view, update, context):
    view.show(update, context)
    assert context.bot.send_message_call


def test_show_edit(view, update, context):
    view.show(update, context, 1)
    assert context.bot.edit_message_text_call


def test_answer(view):
    assert view.get_answer('data') == dict()


def test_process_without_data(view, update, context):
    next_view = deepcopy(view)
    update.callback_query = None
    assert view.process(dict(test_view=next_view), update, context) == view.get_name()


def test_process_with_data(view, update, context):
    next_view = deepcopy(view)
    update.callback_query.data = 'test_view'
    assert view.process(dict(test_view=next_view), update, context) == 'test_view'


def test_process_with_custom_data(view, update, context):
    next_view = deepcopy(view)
    update.callback_query.data = 'omg'
    assert view.process(dict(omg=next_view), update, context) == 'omg'
