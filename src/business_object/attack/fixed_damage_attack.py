# src/business_object/attack/fixed_damage_attack.py
from typing import TYPE_CHECKING

from business_object.attack.abstract_attack import AbstractAttack

if TYPE_CHECKING:
    from business_object.pokemon.abstract_pokemon import AbstractPokemon


class FixedDamageAttack(AbstractAttack):
    """
    An attack that deals a fixed amount of damage (its power),
    regardless of attacker/defender stats.
    """

    def compute_damage(self, attacker: "AbstractPokemon", defender: "AbstractPokemon") -> int:
        return self.power
