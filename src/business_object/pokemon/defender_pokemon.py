from business_object.pokemon.abstract_pokemon import AbstractPokemon


class DefenderPokemon(AbstractPokemon):
    def __init__(self):
        super().__init__()

    def get_pokemon_attack_coef(self) -> float:
        # 1 + (attack + defense) / 200
        return 1 + (self.attack_current + self.defense_current) / 200
