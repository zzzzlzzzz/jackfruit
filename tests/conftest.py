from pytest import fixture


@fixture()
def update():
    class UpdateMock:
        class Chat:
            id = 1

        class CallbackQuery:
            class Message:
                message_id = 1

            def __init__(self):
                self.answer_call = False
                self.message = self.Message()
                self.data = None

            def answer(self, *args, **kwargs):
                self.answer_call = True

        class Message:
            def __init__(self):
                self.text = None
                self.photo = None
                self.audio = None
                self.document = None
                self.video = None

        def __init__(self):
            self.effective_chat = self.Chat()
            self.callback_query = self.CallbackQuery()
            self.message = self.Message()
    yield UpdateMock()


@fixture()
def context():
    class CallbackContextMock:
        chat_data = dict()

        class Bot:
            def __init__(self):
                self.edit_message_text_call = False
                self.send_message_call = False

            def edit_message_text(self, text, chat_id, msg_id, *args, **kwargs):
                self.edit_message_text_call = True

            def send_message(self, chat_id, text, *args, **kwargs):
                self.send_message_call = True

        def __init__(self):
            self.bot = self.Bot()
    yield CallbackContextMock()
