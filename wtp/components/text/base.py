from wtp.components.base import VideoBase

class TextBase(VideoBase):
    def __init__(self, text: str) -> None:
        super().__init__()

        self.text = text
        self.fontSize = 150
        self.font = ""
        self.color = ""
