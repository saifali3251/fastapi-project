from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null, true

from db.base_class import Base

class Job(Base):
  id = Column(Integer,primary_key=True,index=True)
  title = Column(String,nullable=False)
  company = Column(String,nullable=False)
  company_url = Column(String)
  location = Column(String,nullable=False)
  description = Column(String)
  date_posted = Column(Date)
  is_active = Column(Boolean(),default=True)
  owner_id = Column(Integer,ForeignKey('user.id'))  #later user class will be ceated. So owner_id will be FK to user.id
  owner = relationship("User",back_populates="jobs")


'''back_populates means there exist a reverse relationship between owner and jobs'''