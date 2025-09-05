# src/business_object/attack/physical_formula_attack.py
from typing import TYPE_CHECKING

from business_object.attack.abstract_formula_attack import AbstractFormulaAttack

if TYPE_CHECKING:
    from business_object.pokemon.abstract_pokemon import AbstractPokemon


class PhysicalFormulaAttack(AbstractFormulaAttack):
    """
    Attaque physique : Att=attack_current, Def=defense_current
    """

    def get_attack_stat(self, attacker: "AbstractPokemon") -> float:
        return attacker.attack_current

    def get_defense_stat(self, defender: "AbstractPokemon") -> float:
        return defender.defense_current
