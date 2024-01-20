from moviepy.editor import VideoClip
from moviepy.editor import concatenate_videoclips

from wtp.repository.pokemon import PokemonRepository

from wtp.components.base import VideoBase

from wtp.components.question import Question
from wtp.components.answer import Answer

class Video(VideoBase):
    def __init__(self) -> None:
        super().__init__()

        self.repo = PokemonRepository()
        self.pokemon = self.repo.getRandom()
        self.question = Question(self.pokemon)
        self.answer = Answer(self.pokemon)

    def build(self) -> VideoClip:
        return concatenate_videoclips([ 
            self.question.build(), 
            self.answer.build() 
        ])
