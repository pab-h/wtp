from moviepy.editor import VideoClip
from moviepy.editor import ImageClip

from wtp.components.base import VideoBase

class Background(VideoBase):
    def __init__(self) -> None:
        super().__init__()

        self.path = "./wtp/assets/background.png"

    def build(self) -> VideoClip:
        return ImageClip(self.path)