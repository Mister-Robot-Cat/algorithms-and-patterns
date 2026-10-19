"""Strategy Pattern implementation for serialization formats."""
from abc import ABC, abstractmethod
import json
from typing import Dict, Any

class SerializationStrategy(ABC):
    @abstractmethod
    def serialize(self, data: Dict[str, Any]) -> str:
        pass

class JSONStrategy(SerializationStrategy):
    def serialize(self, data: Dict[str, Any]) -> str:
        return json.dumps(data, indent=2)

class KeyValueStrategy(SerializationStrategy):
    def serialize(self, data: Dict[str, Any]) -> str:
        return "\n".join(f"{k}={v}" for k, v in data.items())

class SerializerContext:
    def __init__(self, strategy: SerializationStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: SerializationStrategy) -> None:
        self.strategy = strategy

    def export(self, data: Dict[str, Any]) -> str:
        return self.strategy.serialize(data)
