# src/business_object/attack/abstract_attack.py
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from business_object.pokemon.abstract_pokemon import AbstractPokemon


class AbstractAttack(ABC):
    """
    Base class for all attacks.
    Child classes must implement compute_damage(attacker, defender).
    """

    def __init__(self, power: int, name: str, description: str = ""):
        if power is None or int(power) < 0:
            raise ValueError("power must be a non-negative integer")
        self._power = int(power)
        self._name = name
        self._description = description

    @abstractmethod
    def compute_damage(self, attacker: "AbstractPokemon", defender: "AbstractPokemon") -> int:
        """Return the damage dealt by this attack."""
        pass

    # --- Read-only properties ---
    @property
    def power(self) -> int:
        return self._power

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description
