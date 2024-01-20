from wtp.components.audio.base import AudioBase

class QuestionAudio(AudioBase):
    def __init__(self) -> None:
        super().__init__()

        self.path = "./wtp/assets/whosthatpokemon.mp3"