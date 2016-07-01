import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime 

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

import psycopg2
import urlparse

Base = declarative_base()
##Config Ends##
class Queries (Base):
	__tablename__= 'query'
	query = Column(String(300),nullable= False)
	id = Column(Integer, primary_key = True)
	time = Column(DateTime,nullable= False)
	@property
	def serialize(self):
		return {
		'query' : self.query,
		'time' : self.time
		}
	
##END OF FILE##
engine = create_engine('postgres://jmmodrydkyhole:HOD93bvzChb_zpa30S1ScrHvsE@ec2-54-221-235-135.compute-1.amazonaws.com:5432/d323kk8ffr81ad')

Base.metadata.create_all(engine)
