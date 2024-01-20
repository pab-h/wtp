from abc import ABC
from abc import abstractmethod

from moviepy.editor import VideoClip

class VideoBase(ABC):
    @abstractmethod
    def build(self) -> VideoClip:
        raise NotImplementedError()
    