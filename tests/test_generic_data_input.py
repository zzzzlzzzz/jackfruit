from pytest import fixture

from jackfruit import GenericDataInputView


@fixture()
def view():
    class GenericDataInputViewMock(GenericDataInputView):
        pass
    yield GenericDataInputViewMock()


def test_user_input(view, update):
    assert not view.get_user_input(update)


def test_process_data(view, update, context):
    assert view.process_data(dict(), update, context, None) == view.get_name()


def test_process_without_data(view, update, context):
    view.get_user_input = lambda *args, **kwargs: None
    view.process_data = lambda *args, **kwargs: 'success'
    assert view.process(dict(success=view), update, context) == view.get_name()


def test_process_with_data(view, update, context):
    view.get_user_input = lambda *args, **kwargs: 'user_data'
    view.process_data = lambda *args, **kwargs: 'success'
    assert view.process(dict(success=view), update, context) == 'success'
