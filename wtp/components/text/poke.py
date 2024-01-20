from moviepy.editor import VideoClip
from moviepy.editor import CompositeVideoClip

from wtp.components.text.base import TextBase
from wtp.components.text.hollow import Hollow
from wtp.components.text.solid import Solid

class Poke(TextBase):
    def __init__(self, text: str) -> None:
        super().__init__(text)

        self.hollow = Hollow(self.text)
        self.solid = Solid(self.text)

    def build(self) -> VideoClip:
        return CompositeVideoClip([ 
            self.solid.build(), 
            self.hollow.build() 
        ])
