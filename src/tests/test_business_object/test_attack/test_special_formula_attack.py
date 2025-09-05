# src/tests/test_business_object/test_attack/test_special_formula_attack.py
from unittest.mock import patch

from business_object.attack.special_formula_attack import SpecialFormulaAttack
from business_object.pokemon.all_rounder_pokemon import AllRounderPokemon
from business_object.pokemon.defender_pokemon import DefenderPokemon
from business_object.statistic import Statistic


class TestSpecialFormulaAttack:
    @patch("business_object.attack.abstract_formula_attack.random.uniform", return_value=1.0)
    def test_compute_damage_special(self, _mock_uniform):
        # GIVEN
        # Level=50, Power=100, Att(sp_atk)=100, Def(sp_def)=100 -> base = 46
        attack = SpecialFormulaAttack(power=100, name="Psybeam")
        attacker = AllRounderPokemon(stat_current=Statistic(sp_atk=100), level=50)
        defender = DefenderPokemon(stat_current=Statistic(sp_def=100))

        # WHEN
        damage = attack.compute_damage(attacker, defender)

        # THEN
        assert damage == 46
