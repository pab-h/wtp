import pokebase as pb

from random import random

from wtp.entities.pokemon import Pokemon

from PIL import Image

from uuid import uuid4 as uuid

class PokemonRepository:
    def __init__(self) -> None:
        self.amout = 1302

    def shadownSprite(self, path: str) -> str:
        with Image.open(path) as pokemonImage:
            pokemonImage = pokemonImage.convert("RGBA")

            width, height = pokemonImage.size

            for i in range(width):
                for j in range(height):
                    r, g, b, a = pokemonImage.getpixel((i, j))

                    if a != 0:
                        pokemonImage.putpixel((i, j), (0, 0, 0, 255))
                    
            pokemonImage.save(f"./.tmp/{ uuid() }.png")

    def getRandom(self) -> Pokemon:
        response = pb.pokemon(random() * self.amout)

        spriteShadow = self.shadownSprite(response.path)

        return Pokemon(
            name = response.name,
            sprite = response.path,
            spriteShadow = spriteShadow
        )
