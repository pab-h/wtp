from abc import ABC

from moviepy.editor import AudioClip
from moviepy.editor import AudioFileClip

class AudioBase(ABC):
    def __init__(self) -> None:
        self.path = ""

    def build(self) -> AudioClip:
        return AudioFileClip(self.path)