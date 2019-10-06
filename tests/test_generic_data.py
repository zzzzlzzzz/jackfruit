from pytest import fixture

from jackfruit import GenericDataInputView


@fixture()
def view():
    class GenericDataInputViewMock(GenericDataInputView):
        pass
    yield GenericDataInputViewMock()


def test_show_without_prev(view, update, context):
    view.show(update, context)
    assert context.bot.send_message_call


def test_show_with_prev(view, update, context):
    view.show(update, context, 1)
    assert context.bot.edit_message_text_call
