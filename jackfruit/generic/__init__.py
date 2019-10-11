from .generic import GenericView, GenericDataInputView
from .menu import MenuView
from .text import TextDataInputView
from .photo import PhotoDataInputView
from .audio import AudioDataInputView
from .document import DocumentDataInputView
from .video import VideoDataInputView
from .sticker import StickerDataInputView

__all__ = ['GenericView', 'GenericDataInputView', 'MenuView', 'TextDataInputView', 'PhotoDataInputView',
           'AudioDataInputView', 'DocumentDataInputView', 'VideoDataInputView', 'StickerDataInputView', ]
