from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

@dataclass(frozen=True)
class ShapeRecord(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def __init__(self, **kwargs) -> None:
        self.id = kwargs["id"]
        self.name = kwargs["name"]
    
    def __eq__(self, user: InkyUser) -> bool:
        return self.__hash__() == user.__hash__()
    
    def __hash__(self):
        return hash((self.id,
                     self.name
        ))

engine = create_engine('sqlite:///shape_db.sqlite3')
Base.metadata.create_all(engine)