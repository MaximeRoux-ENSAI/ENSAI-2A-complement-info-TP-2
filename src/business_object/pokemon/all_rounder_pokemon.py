from business_object.pokemon.abstract_pokemon import AbstractPokemon


class AllRounderPokemon(AbstractPokemon):
    def __init__(self):
        super().__init__()

    def get_pokemon_attack_coef(self) -> float:
        # 1 + (sp_atk + sp_def) / 200
        return 1 + (self.sp_atk_current + self.sp_def_current) / 200
