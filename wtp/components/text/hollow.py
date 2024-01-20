from moviepy.editor import VideoClip
from moviepy.editor import TextClip

from wtp.components.text.base import TextBase

class Hollow(TextBase):
    def __init__(self, text: str) -> None:
        super().__init__(text)

        self.color = "blue"
        self.font = "./wtp/assets/Pokemon Hollow.ttf"

    def build(self) -> VideoClip:
        return TextClip(
            txt = self.text,
            font = self.font,
            fontsize = self.fontSize,
            color = self.color
        )
    