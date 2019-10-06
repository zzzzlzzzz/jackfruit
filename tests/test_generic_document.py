from pytest import fixture

from jackfruit import DocumentDataInputView


@fixture()
def view():
    class DocumentDataInputViewMock(DocumentDataInputView):
        pass
    yield DocumentDataInputViewMock()


def test_get_user_input(view, update):
    class DocumentMock:
        pass
    update.message.document = DocumentMock()
    assert view.get_user_input(update) == update.message.document


def test_get_user_input_without_message(view, update):
    update.message = None
    assert not view.get_user_input(update)


def test_get_user_input_without_document(view, update):
    assert not view.get_user_input(update)
