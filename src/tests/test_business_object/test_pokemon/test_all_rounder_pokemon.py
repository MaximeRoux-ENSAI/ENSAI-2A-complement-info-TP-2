from business_object.pokemon.all_rounder_pokemon import AllRounderPokemon
from business_object.statistic import Statistic


class TestAllRounderPokemon:
    def test_get_coef_damage_type(self):
        # GIVEN
        # Formula: 1 + (sp_atk + sp_def) / 200
        charizard = AllRounderPokemon(stat_current=Statistic(sp_atk=50, sp_def=150))

        # WHEN
        multiplier = charizard.get_pokemon_attack_coef()

        # THEN
        # Expected: 1 + (50 + 150) / 200 = 1 + 200/200 = 2
        assert multiplier == 2


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
