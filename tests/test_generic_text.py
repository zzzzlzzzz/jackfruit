from pytest import fixture

from jackfruit import TextDataInputView


@fixture()
def view():
    class TextInputViewMock(TextDataInputView):
        pass
    yield TextInputViewMock()


def test_get_user_input(view, update):
    update.message.text = 'data'
    assert view.get_user_input(update) == update.message.text


def test_get_user_input_without_message(view, update):
    update.message = None
    assert not view.get_user_input(update)


def test_get_user_input_without_text(view, update):
    assert not view.get_user_input(update)


def test_process_data(view, update, context):
    assert view.process_data(dict(), update, context, 'data') == view.get_name()


def test_show(view, update, context):
    view.show(update, context)
    assert context.bot.send_message_call


def test_show_edit(view, update, context):
    view.show(update, context, 1)
    assert context.bot.edit_message_text_call


def test_process_without_data(view, update, context):
    view.process_data = lambda *args, **kwargs: 'processed'
    assert view.process(dict(processed=view), update, context) == view.get_name()


def test_process_with_data(view, update, context):
    view.process_data = lambda *args, **kwargs: 'processed'
    update.message.text = 'Data'
    assert view.process(dict(processed=view), update, context) == 'processed'
