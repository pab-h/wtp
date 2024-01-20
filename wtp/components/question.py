from moviepy.editor import VideoClip
from moviepy.editor import CompositeVideoClip
from moviepy.editor import ImageClip

from moviepy.video.fx.margin import margin

from wtp.entities.pokemon import Pokemon

from wtp.components.text.poke import Poke
from wtp.components.audio.question import QuestionAudio
from wtp.components.base import VideoBase
from wtp.components.background import Background

class Question(VideoBase):
    def __init__(self, pokemon: Pokemon) -> None:
        super().__init__()

        self.pokemon = pokemon
        self.background = Background()
        self.whothatText = Poke("Who's That")
        self.pokemonText = Poke("Pokémon?")
        self.questionAudio = QuestionAudio()

    def build(self) -> VideoClip:
        whothatText = self.whothatText.build()
        whothatText = whothatText.set_position(("center", "top"))
        whothatText = margin(
            clip = whothatText, 
            top = 125,
            opacity = 0
        )

        pokemonText = self.pokemonText.build()
        pokemonText = pokemonText.set_position(("center", "bottom"))
        pokemonText = margin(
            clip = pokemonText, 
            bottom = 175,
            opacity = 0
        )

        pokemonShadow = ImageClip(self.pokemon.spriteShadow)
        pokemonShadow = pokemonShadow.set_position(("center", "center"))

        video = CompositeVideoClip([
            self.background.build(),
            whothatText,
            pokemonText,
            pokemonShadow
        ])
        video = video.set_duration(6)
        video = video.set_fps(30)

        audio = self.questionAudio.build() 
        
        video = video.set_audio(audio)

        return video
