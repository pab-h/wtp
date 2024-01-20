import pokebase as pb

from random import random

from wtp.entities.pokemon import Pokemon

from PIL import Image

from uuid import uuid4 as uuid

class PokemonRepository:
    def __init__(self) -> None:
        self.amout = 1302

    def prepareSprite(self, path: str) -> str:
        filename = f"./.tmp/{ uuid() }.png"

        with Image.open(path) as image:
            image\
                .convert("RGBA")\
                .resize((960, 960))\
                .save(filename)

        return filename

    def shadownSprite(self, path: str) -> str:
        filename = f"./.tmp/{ uuid() }.png"

        with Image.open(path) as pokemonImage:
            pokemonImage = pokemonImage.convert("RGBA")

            width, height = pokemonImage.size

            for i in range(width):
                for j in range(height):
                    r, g, b, a = pokemonImage.getpixel((i, j))

                    if a != 0:
                        pokemonImage.putpixel((i, j), (0, 0, 0, 255))
                    
            pokemonImage.save(filename)

        return filename

    def getRandom(self) -> Pokemon:
        # randomId = int(random() * self.amout)
        randomId = 1

        pokemonSprite = pb.SpriteResource('pokemon', randomId)
        pokemon = pb.pokemon(randomId)

        spritePrepared = self.prepareSprite(pokemonSprite.path)
        spriteShadow = self.shadownSprite(spritePrepared)

        return Pokemon(
            name = pokemon.name,
            sprite = spritePrepared,
            spriteShadow = spriteShadow
        )
