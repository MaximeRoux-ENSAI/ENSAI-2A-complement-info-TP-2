# src/tests/test_business_object/test_attack/test_fixed_damage_attack.py
import pytest

from business_object.attack.fixed_damage_attack import FixedDamageAttack
from business_object.pokemon.attacker_pokemon import AttackerPokemon
from business_object.pokemon.defender_pokemon import DefenderPokemon
from business_object.statistic import Statistic


class TestFixedDamageAttack:
    def test_compute_damage_returns_power(self):
        # GIVEN
        attack = FixedDamageAttack(power=42, name="Tackle", description="Fixed dmg")
        attacker = AttackerPokemon(stat_current=Statistic())  # any pokemon works
        defender = DefenderPokemon(stat_current=Statistic())

        # WHEN
        damage = attack.compute_damage(attacker, defender)

        # THEN
        assert damage == 42

    def test_power_must_be_non_negative(self):
        with pytest.raises(ValueError):
            FixedDamageAttack(power=-1, name="Glitch")

    def test_accessors(self):
        atk = FixedDamageAttack(power=10, name="Ping", description="Pong")
        assert atk.power == 10
        assert atk.name == "Ping"
        assert atk.description == "Pong"
