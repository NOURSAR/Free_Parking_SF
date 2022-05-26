"""Models for Free On_Street Searching."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Parking(db.Model):
    """requesting data from soda Api
    On-Street Parking Census
    """

    __tablename__ = "parkings"

    parking_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cnn = db.Column(db.Float)
    st_name = db.Column(db.String)
    st_type = db.Column(db.String)
    district = db.Column(db.String)
    prkg_sply=db.Column(db.Integer)
    collectn= db.Column(db.String)
    year= db.Column(db.Integer)

    def __repr__(self):
        return f"<Parking parking_id={self.parking_id} st_name={self.st_name} cnn={self.cnn} st_type={self.st_type} district={self.district} prkg_sply={self.prkg_sply} collectn={self.collectn} year={self.year}"


class Coordinate(db.Model):
    """ list of coordinates"""

    __tablename__ = "coordinates"

    coordinate_id= db.Column(db.Integer, autoincrement=True, primary_key=True)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)

    parking_id = db.Column(db.Integer, db.ForeignKey("parkings.parking_id"))
    parking= db.relationship("Parking", backref="coordinates")
  

    def __repr__(self):
        return f"<Coordinate lat={self.lat} lon={self.lon}"


# class Regulation(db.Model):
#     """Parking regulations (except non-metered color curb)"""

#     __tablename__ = "regulations"

#     reg_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     agency = db.Column(db.Integer)
#     regulation = db.Column(db.String)
#     days = db.Column(db.String)
#     hours= db.Column(db.String)
#     hrs_begin= db.Column(db.String)
#     hrs_end= db.Column(db.String)
#     regdetails = db.Column(db.String)
#     modified = db.Column(db.String)
#     editor = db.Column(db.String)
#     rpparea1 = db.Column(db.String)
#     rpparea2 = db.Column(db.String)
#     rpparea3 = db.Column(db.String)
#     fid_100= db.Column(db.String)
#     length_ft = db.Column(db.Integer)
#     conflict = db.Column(db.String)
#     enacted = db.Column(db.String)
#     created_us= db.Column(db.String)
#     created_da= db.Column(db.String)
#     last_edi_1= db.Column(db.String)
#     last_edite= db.Column(db.String)
#     hrlimit = db.Column(db.String)
#     created_user = db.Column(db.String)
#     created_date= db.Column(db.String)
#     last_edited_user= db.Column(db.String)
#     last_edited_date = db.Column(db.String)
#     rpp_sym= db.Column(db.String)
#     mtab_date= db.Column(db.String)
#     mtab_motion= db.Column(db.String)
#     mtab_reso_text= db.Column(db.String)
#     sym_rpp2= db.Column(db.String)
#     globalid= db.Column(db.String)
#     exceptions= db.Column(db.String)
#     from_time = db.Column(db.String)
#     to_time= db.Column(db.String)
#     # shape = db.Column(db.Multiline)


#     def __repr__(self):
#         return f"<Regulation regulation={self.regulation}"

# class Sweep(db.Model):
#     """Street Sweeping Schedule"""
#     __tablename__ = "sweeping_times"

#     sweep_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     cnn = db.Column(db.Integer)
#     corridor = db.Column(db.String)
#     limits = db.Column(db.String)
#     cnnrightleft = db.Column(db.String)
#     blockside = db.Column(db.String)
#     fullname = db.Column(db.String)
#     weekday = db.Column(db.String)
#     fromhour = db.Column(db.Integer)
#     tohour = db.Column(db.Integer)
#     week1 = db.Column(db.Integer)
#     week2 = db.Column(db.Integer)
#     week3 = db.Column(db.Integer)
#     week4 = db.Column(db.Integer)
#     week5 = db.Column(db.Integer)
#     holidays = db.Column(db.Integer)
#     blocksweepid = db.Column(db.Integer)
#     # line = db.Column(db.Line)

#     req_id = db.Column(db.Integer, db.ForeignKey("requests.req_id"))
#     response = db.relationship("Request", backref="sweep")
    
#     def __repr__(self):
#         return f"<Sweep corridor={self.corridor}>"

# class Request(db.Model):
#     """returns requestes."""

#     __tablename__ = "requests"

#     req_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     request = db.Column(db.String)
#     parking_id = db.Column(db.Integer,db.ForeignKey("parkings.parking_id") )


#     parking = db.relationship("Parking", backref="response")
#     sweep = db.relationship("Sweep", backref="response")
#     Coordinate = db.relationship("Coordinate", backref="response")
#     regulation = db.relationship("Regulation", backref="response")


#     def __repr__(self):
#         return f"<Request request={self.request}>"


#### Nice to have


# class User(db.Model):
#     """A user."""

#     __tablename__ = "users"

#     user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     email = db.Column(db.String, unique=True)
#     password = db.Column(db.String)

#     request = db.relationship("Request", backref="requests")

#     def __repr__(self):
#         return f"<User user_id={self.user_id} email={self.email}>" 


# class Favourite(db.Model):
#     """A favourited Parking."""

#     __tablename__ = "Favourites"

#     favourite_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     parking_id = db.Column(db.Integer, db.ForeignKey("parkings.parking_id"))
#     user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

#     parking = db.relationship("Parking", backpopulates="parkings")
#     user = db.relationship("User", backpopulates="favourites")

#     def __repr__(self):
#         return f"<Favourite favourite_id={self.favourite_id}>"


def connect_to_db(flask_app, db_uri="postgresql:///onstreetparking", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


# if __name__ == "__main__":
from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.
connect_to_db(app)
