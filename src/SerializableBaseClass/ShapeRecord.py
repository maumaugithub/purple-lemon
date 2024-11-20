from dataclasses import dataclass

@dataclass(frozen=True)
class ShapeRecord:
    id: int
    name: str
    price: float
    
    def __eq__(self, shape: ShapeRecord) -> bool:
        return self.__hash__() == shape.__hash__()

    def __hash__(self):
        return hash((self.id, self.name))