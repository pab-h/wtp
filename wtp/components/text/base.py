from wtp.components.base import VideoBase

from moviepy.editor import VideoClip

class TextBase(VideoBase):
    def __init__(self, text: str) -> None:
        super().__init__()

        self.text = text
        self.fontSize = 150
        self.font = ""
        self.color = ""

    def build(self) -> VideoClip:
        return super().build()
