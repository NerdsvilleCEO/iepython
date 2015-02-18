#!/usr/bin/python2.7
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from imagedb import Image

engine = create_engine("sqlite:///images.db", echo=True)

#Create a new session
session = sessionmaker(bind=engine)
session = session()

#Create a record
image = Image(sourceUrl = "test",
              dateRetrieved = datetime.datetime.now(),
              latitude = "test",
              longitude = "test",
              imageDate = datetime.datetime.now(),
              imageWidth = 100,
              imageHeight = 100,
              imageFile = "test")

#Add the record to the database
session.add(image)
#Commit and close the database session
session.commit()
session.close()