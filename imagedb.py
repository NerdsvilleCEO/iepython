#!/usr/bin/python2.7
from sqlalchemy import Column, Date, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

#Declarative Base does the mapping between class names and fields in table

Base = declarative_base()
class Image(Base):
    #Name of table
    __tablename__ = "images"
    
    #Attributes of table
    id = Column(Integer, primary_key=True)
    sourceUrl = Column(String)
    dateRetrieved = Column(Date)
    latitude = Column(String)
    longitude = Column(String)
    imageDate = Column(Date)
    imageWidth = Column(Integer)
    imageHeight = Column(Integer)
    imageFile = Column(String)

    #Constructor Function
    def __init__(self, *args, **kargs):
    	#Instantiate super class called Base for sqlalchemy, and pass in the dict of keyword args and args
    	super(Image, self).__init__(*args, **kargs)
        self.imageWidth = kargs.get("imageWidth")

#Use sqlite engine and create table
engine = create_engine('sqlite:///images.db', echo=True)
Base.metadata.create_all(engine)