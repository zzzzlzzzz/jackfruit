from pytest import fixture, mark

from jackfruit import (GenericDataInputView, AudioDataInputView, DocumentDataInputView, PhotoDataInputView,
                       StickerDataInputView, TextDataInputView, VideoDataInputView)


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


@mark.parametrize('test_class,message_attr',
                  [
                      (AudioDataInputView, 'audio'),
                      (DocumentDataInputView, 'document'),
                      (PhotoDataInputView, 'photo'),
                      (StickerDataInputView, 'sticker'),
                      (TextDataInputView, 'text'),
                      (VideoDataInputView, 'video'),
                  ])
def test_data_input_view(test_class, message_attr, update):
    class MessageAttrMock:
        pass
    setattr(update.message, message_attr, MessageAttrMock())
    assert test_class().get_user_input(update) == getattr(update.message, message_attr)


@mark.parametrize('test_class',
                  [
                      AudioDataInputView,
                      DocumentDataInputView,
                      PhotoDataInputView,
                      StickerDataInputView,
                      TextDataInputView,
                      VideoDataInputView,
                  ])
def test_data_input_view_without_message(test_class, update):
    update.message = None
    assert not test_class().get_user_input(update)


@mark.parametrize('test_class',
                  [
                      AudioDataInputView,
                      DocumentDataInputView,
                      PhotoDataInputView,
                      StickerDataInputView,
                      TextDataInputView,
                      VideoDataInputView,
                  ])
def test_data_input_view_without_attr(test_class, update):
    assert not test_class().get_user_input(update)
