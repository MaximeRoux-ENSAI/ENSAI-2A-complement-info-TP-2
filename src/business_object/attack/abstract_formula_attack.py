# src/business_object/attack/abstract_formula_attack.py
import random
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from business_object.attack.abstract_attack import AbstractAttack

if TYPE_CHECKING:
    from business_object.pokemon.abstract_pokemon import AbstractPokemon


class AbstractFormulaAttack(AbstractAttack, ABC):
    """
    Attaque basée sur une formule commune :
        Damage = ( ((2*Level)/5 + 2) * Power * Att / (Def*50) + 2 ) * random
    avec random ~ U[0.85, 1.0].

    Seules les stats Att et Def changent selon le type d'attaque (physique/spéciale).
    """

    def compute_damage(self, attacker: "AbstractPokemon", defender: "AbstractPokemon") -> int:
        att = self.get_attack_stat(attacker)
        deff = self.get_defense_stat(defender)
        if deff <= 0:
            deff = 1  # éviter /0

        # Partie déterministe
        base = ((2 * attacker.level) / 5 + 2) * self.power * att / (deff * 50) + 2

        # Facteur aléatoire
        factor = random.uniform(0.85, 1.0)
        dmg = base * factor

        # On renvoie un int (troncature, comme dans beaucoup de formules simplifiées)
        return int(dmg)

    # -- Méthodes à spécialiser --
    @abstractmethod
    def get_attack_stat(self, attacker: "AbstractPokemon") -> float:
        pass

    @abstractmethod
    def get_defense_stat(self, defender: "AbstractPokemon") -> float:
        pass
