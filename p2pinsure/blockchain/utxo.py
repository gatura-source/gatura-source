from dataclasses import dataclass
from typing import Protocol, List, Optional

@dataclass
class UTXO:
    txid: str  # Transaction ID
    index: int  # Output index
    amount: float  # Amount of the UTXO
    script_pub_key: str  # Public key script of the UTXO

class UTXOSet(Protocol):
    def add_utxo(self, utxo: UTXO) -> None:
        """Add a UTXO to the set."""

    def remove_utxo(self, txid: str, index: int) -> None:
        """Remove a UTXO from the set."""

    def get_utxo(self, txid: str, index: int) -> Optional[UTXO]:
        """Retrieve a UTXO by transaction ID and index."""

    def get_all_utxos(self) -> List[UTXO]:
        """Retrieve all UTXOs in the set."""