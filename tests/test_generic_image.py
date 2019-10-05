from pytest import fixture

from jackfruit import ImageInputView


@fixture()
def view():
    class ImageInputViewMock(ImageInputView):
        pass
    yield ImageInputViewMock()


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
