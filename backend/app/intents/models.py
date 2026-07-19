from dataclasses import dataclass
from typing import Optional


@dataclass
class Intent:
    name: str
    tool: Optional[str]
    confidence: float