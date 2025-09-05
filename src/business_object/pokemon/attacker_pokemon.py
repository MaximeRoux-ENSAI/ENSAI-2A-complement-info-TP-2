from business_object.pokemon.abstract_pokemon import AbstractPokemon


class AttackerPokemon(AbstractPokemon):
    def __init__(self):
        super().__init__()
        
    def get_pokemon_attack_coef(self) -> float:
        # 1 + (speed + attack) / 200
        return 1 + (self.speed_current + self.attack_current) / 200
