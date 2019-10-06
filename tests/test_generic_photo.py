from pytest import fixture

from jackfruit import PhotoDataInputView


@fixture()
def view():
    class PhotoInputViewMock(PhotoDataInputView):
        pass
    yield PhotoInputViewMock()


def test_get_user_input(view, update):
    class PhotoSizeMock:
        pass

    update.message.photo = [PhotoSizeMock(), ]
    assert view.get_user_input(update) == update.message.photo


def test_get_user_input_without_message(view, update):
    update.message = None
    assert not view.get_user_input(update)


def test_get_user_input_without_photo(view, update):
    assert not view.get_user_input(update)



def test_process_data(view, update, context):
    assert view.process_data(dict(), update, context, []) == view.get_name()


def test_process_without_data(view, update, context):
    view.process_data = lambda _: 'processed'
    assert view.process(dict(processed=view), update, context) == view.get_name()


def test_process_with_data(view, update, context):
    class PhotoSizeMock:
        pass
    view.process_data = lambda *args, **kwargs: 'processed'
    update.message.photo = [PhotoSizeMock(), ]
    assert view.process(dict(processed=view), update, context) == 'processed'
