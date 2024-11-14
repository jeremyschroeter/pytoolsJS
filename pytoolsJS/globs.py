from pathlib import Path


class Globs:
    def __init__(self, machine: str) -> None:
        self.machine = machine

        if self.machine == 'macbook':
            NotImplemented