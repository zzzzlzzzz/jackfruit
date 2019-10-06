from typing import Any

from telegram.update import Update

from .generic import GenericDataInputView


class DocumentDataInputView(GenericDataInputView):
    def get_user_input(self, update: 'Update') -> Any:
        try:
            return update.message.document
        except AttributeError:
            return None
