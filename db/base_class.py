from typing import Any
from sqlalchemy.ext.declarative import as_declarative,declared_attr

@as_declarative()
class Base:
  id: Any
  __name__ : str


  @declared_attr
  def __tablename__(cls)->str:
    return cls.__name__.lower()

'''So we dont need to declare table name and id for each and every class. Every class will inherit this base_class'''