#!/usr/bin/python2.7
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from imagedb import Image

engine = create_engine("sqlite:///images.db")

#Create a session
Session = sessionmaker(bind=engine)
session = Session()

#Read records
image = session.query(Image).filter(Image.imageWidth>50).all()
print image[0].sourceUrl
session.close()
