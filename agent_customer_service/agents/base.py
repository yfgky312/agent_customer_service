from abc import ABC, abstractmethod
from config import llm
from state import state


class BaseAgent(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def run(self, context: dict) -> dict:
        pass

    def _call_llm(self, prompt: str) -> str:
        response = llm.invoke(prompt)
        return response.content

    def _log(self, msg: str):
        print(f"[{self.name}] {msg}")