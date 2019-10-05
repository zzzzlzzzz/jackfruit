from pytest import fixture

from telegram import ParseMode

from jackfruit import GenericView


@fixture()
def view():
    class GenericViewMock(GenericView):
        disable_web_page_preview = True
        parse_mode = ParseMode.MARKDOWN
        text = 'test'
    yield GenericViewMock()


def test_name(view):
    assert view.get_name() == view.__class__.__name__


def test_get_disable_web_page_preview(view):
    assert view.get_disable_web_page_preview()


def test_parse_mode(view):
    assert view.get_parse_mode() == ParseMode.MARKDOWN


def test_get_text(view):
    assert view.get_text() == 'test'


def test_show(view, update, context):
    assert view.show(update, context) is None


def test_process(view, update, context):
    assert view.process(dict(), update, context) == view.get_name()
