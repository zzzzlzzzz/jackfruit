from pytest import fixture

from jackfruit import AudioDataInputView


@fixture()
def view():
    class AudioDataInputViewMock(AudioDataInputView):
        pass
    yield AudioDataInputViewMock()


def test_get_user_input(view, update):
    class AudioMock:
        pass
    update.message.audio = AudioMock()
    assert view.get_user_input(update) == update.message.audio


def test_get_user_input_without_message(view, update):
    update.message = None
    assert not view.get_user_input(update)


def test_get_user_input_without_audio(view, update):
    assert not view.get_user_input(update)
