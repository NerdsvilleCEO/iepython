#!/usr/bin/python2.7
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from imagedb import Image

engine = create_engine("sqlite:///images.db", echo=True)

#Create a session
Session = sessionmaker(bind = engine)
session = Session()

#Update first record
image = session.query(Image).filter(Image.imageWidth>50).all()
image[0].sourceUrl = "testing123"
session.flush()
session.commit()
session.close()
