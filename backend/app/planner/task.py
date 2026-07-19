from dataclasses import dataclass


@dataclass
class Task:
    action: str
    target: str
    status: str = "pending"