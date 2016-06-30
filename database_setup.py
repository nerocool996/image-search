import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String 

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

import psycopg2
import urlparse

Base = declarative_base()
##Config Ends##
class Links (Base):
	__tablename__= 'links'
	url = Column(String(300),nullable= False)
	id = Column(Integer, primary_key = True)
	short_URL = Column(String(300),nullable= False)
	@property
	def serialize(self):
		return {
		'URL' : self.url,
		'id' : self.id,
		'shortURL' : self.short_URL
		}
	
##END OF FILE##
engine = create_engine('postgres://eftouahahwepdz:L1bqXJw6TrrHoASeNh8XmjpgRB@ec2-54-243-212-72.compute-1.amazonaws.com:5432/d56424prqdm2cu')

Base.metadata.create_all(engine)
