from pytest import fixture

from jackfruit import VideoDataInputView


@fixture()
def view():
    class VideoDataInputViewMock(VideoDataInputView):
        pass
    yield VideoDataInputViewMock()


def test_get_user_input(view, update):
    class VideoMock:
        pass
    update.message.video = VideoMock()
    assert view.get_user_input(update) == update.message.video


def test_get_user_input_without_message(view, update):
    update.message = None
    assert not view.get_user_input(update)


def test_get_user_input_without_video(view, update):
    assert not view.get_user_input(update)
