from moviepy.editor import VideoClip
from moviepy.editor import TextClip

from wtp.components.text.base import TextBase

class Solid(TextBase):
    def __init__(self, text: str) -> None:
        super().__init__(text)

        self.color = "yellow"
        self.font = "./wtp/assets/Pokemon Solid.ttf"

    def build(self) -> VideoClip:
        return TextClip(
            txt = self.text,
            font = self.font,
            fontsize = self.fontSize,
            color = self.color
        )
    