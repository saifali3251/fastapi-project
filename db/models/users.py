from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


'''User class inherits the base class that we created'''
class User(Base):
  id = Column(Integer,primary_key=True,index=True)
  username = Column(String,unique=True,nullable=False)
  email = Column(String,nullable=False,unique=True,index=True) #index we used for future use. We'll be searching based on email
  hashed_password = Column(String,nullable=False)
  is_active = Column(Boolean(),default=True)
  is_superuser = Column(Boolean(),default=False)
  jobs = relationship("Job",back_populates="owner")
