from wtp.entities.pokemon import Pokemon
from wtp.components.audio.base import AudioBase

from gtts import gTTS

from uuid import uuid4 as uuid

class PokeNameAudio(AudioBase):
    def __init__(self, pokemon: Pokemon) -> None:
        super().__init__()

        self.pokemon = pokemon
        self.path = f"./.tmp/{ uuid() }.mp3"

        gTTS(
            text = f"It's { self.pokemon.name }", 
            lang = "en"
        ).save(self.path) 
