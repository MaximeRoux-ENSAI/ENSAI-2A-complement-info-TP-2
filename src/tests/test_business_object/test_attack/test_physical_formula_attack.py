# src/tests/test_business_object/test_attack/test_physical_formula_attack.py
from unittest.mock import patch

from business_object.attack.physical_formula_attack import PhysicalFormulaAttack
from business_object.pokemon.attacker_pokemon import AttackerPokemon
from business_object.pokemon.defender_pokemon import DefenderPokemon
from business_object.statistic import Statistic


class TestPhysicalFormulaAttack:
    @patch("business_object.attack.abstract_formula_attack.random.uniform", return_value=1.0)
    def test_compute_damage_physical(self, _mock_uniform):
        # GIVEN
        # Level=50, Power=100, Att=100, Def=100 -> base = 46 exact
        attack = PhysicalFormulaAttack(power=100, name="Slam")
        attacker = AttackerPokemon(stat_current=Statistic(attack=100), level=50)
        defender = DefenderPokemon(stat_current=Statistic(defense=100))

        # WHEN
        damage = attack.compute_damage(attacker, defender)

        # THEN
        assert damage == 46

    @patch("business_object.attack.abstract_formula_attack.random.uniform", return_value=0.85)
    def test_random_factor_applied(self, _mock_uniform):
        # GIVEN même setup
        attack = PhysicalFormulaAttack(power=100, name="Slam")
        attacker = AttackerPokemon(stat_current=Statistic(attack=100), level=50)
        defender = DefenderPokemon(stat_current=Statistic(defense=100))

        # base = 46 puis *0.85 -> 39.1 -> int() = 39
        damage = attack.compute_damage(attacker, defender)
        assert damage == 39
