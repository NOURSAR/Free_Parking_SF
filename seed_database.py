import os
import json
import crud
import model
import server

os.system('dropdb onstreetparking')
os.system('createdb onstreetparking')

model.connect_to_db(server.app)
model.db.create_all()

# model.db.session.add_all()
# model.db.session.commit()
