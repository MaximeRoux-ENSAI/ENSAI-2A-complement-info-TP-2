# src/business_object/attack/special_formula_attack.py
from typing import TYPE_CHECKING

from business_object.attack.abstract_formula_attack import AbstractFormulaAttack

if TYPE_CHECKING:
    from business_object.pokemon.abstract_pokemon import AbstractPokemon


class SpecialFormulaAttack(AbstractFormulaAttack):
    """
    Attaque spéciale : Att=sp_atk_current, Def=sp_def_current
    """

    def get_attack_stat(self, attacker: "AbstractPokemon") -> float:
        return attacker.sp_atk_current

    def get_defense_stat(self, defender: "AbstractPokemon") -> float:
        return defender.sp_def_current
