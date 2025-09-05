from business_object.pokemon.abstract_pokemon import AbstractPokemon
from business_object.statistic import Statistic


class DefenderPokemon(AbstractPokemon):
    def __init__(
        self,
        stat_max: Statistic = None,
        stat_current: Statistic = None,
        level: int = 0,
        name: str = None,
    ):
        super().__init__(
            stat_max=stat_max,
            stat_current=stat_current,
            level=level,
            name=name,
        )

    def get_pokemon_attack_coef(self) -> float:
        # 1 + (attack + defense) / 200
        return 1 + (self.attack_current + self.defense_current) / 200
