from moviepy.editor import VideoClip
from moviepy.editor import CompositeVideoClip
from moviepy.editor import ImageClip

from moviepy.video.fx.margin import margin
from moviepy.video.fx.fadein import fadein

from wtp.entities.pokemon import Pokemon

from wtp.components.text.poke import Poke
from wtp.components.base import VideoBase
from wtp.components.background import Background
from wtp.components.audio.pokename import PokeNameAudio

class Question(VideoBase):
    def __init__(self, pokemon: Pokemon) -> None:
        super().__init__()

        self.pokemon = pokemon
        self.background = Background()
        self.pokemonNameText = Poke(self.pokemon.name)
        self.pokemonNameAudio = PokeNameAudio(self.pokemon)

    def build(self) -> VideoClip:
        pokemonNameText = self.pokemonNameText.build()
        pokemonNameText = margin(
            clip = pokemonNameText, 
            bottom = 175,
            opacity = 0
        )

        pokemonImage = ImageClip(self.pokemon.sprite)
        pokemonImage = pokemonImage.resize(10)
        pokemonImage = pokemonImage.set_position(("center", "center"))

        video = CompositeVideoClip([
            self.background.build(),
            pokemonNameText,
            pokemonImage
        ])
        video = video.set_fps(30)

        audio = self.pokemonNameAudio.build()
        
        video = video.set_duration(audio.duration + 2)
        video = video.set_audio(audio)
        video = fadein(video, 0.5)

        return video
