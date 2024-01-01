from pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon in self.pokemons:
            return 'This pokemon is already caught'
        else:
            self.pokemons.append(pokemon)
            return f'Caught {pokemon.pokemon_details()}'

    def release_pokemon(self, pokemon_name: str):
        # [self.pokemons.remove(pokemon) for pokemon in self.pokemons if pokemon_name == pokemon.name]
        for pokemon in self.pokemons:
            if pokemon.name == pokemon_name:
                self.pokemons.remove(pokemon)
                return f'You have released {pokemon_name}'

        return 'Pokemon is not caught'

    def trainer_data(self) -> str:
        result = []
        result.append(f'Pokemon Trainer {self.name}')
        result.append(f'Pokemon count {len(self.pokemons)}')
        [result.append(f'- {pokemon.pokemon_details()}') for pokemon in self.pokemons]

        return '\n'.join(result)
