# src/tests/test_business_object/test_pokemon/test_abstract_pokemon_levelup.py
from business_object.pokemon.abstract_pokemon import AbstractPokemon
from business_object.statistic import Statistic


class _DummyPokemon(AbstractPokemon):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_pokemon_attack_coef(self) -> float:
        return 1.0  # implémentation minimale


def test_level_up_increments_level():
    # GIVEN
    p = _DummyPokemon(stat_current=Statistic(), level=0)

    # WHEN
    p.level_up()

    # THEN
    assert p.level == 1
