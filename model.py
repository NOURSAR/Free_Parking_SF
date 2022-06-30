from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Parking(db.Model):
    """Parkings by users"""

    __tablename__ = "parkings"

    parking_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    st_name = db.Column(db.String, nullable=False)
    cross_st_1= db.Column(db.String, nullable=False)
    cross_st_2 = db.Column(db.String, nullable=False)
    address=db.Column(db.String, nullable=False)
    longtitude= db.Column(db.Float, nullable=False)
    latitude= db.Column(db.Float, nullable=False)

    #reviews

    def __repr__(self):
        return f"<Parking parking_id={self.parking_id} st_name={self.st_name}" 
  
#### Nice to have


class User(UserMixin, db.Model):
    """A user."""

    __tablename__ = "users"
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(130))
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    #reviews

    def __repr__(self):
        return f"<User user_id={self.id} email={self.email}>" 


class Review(db.Model):
    """A rated parking."""

    __tablename__ = "reviews"

    review_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    parking_id = db.Column(db.Integer, db.ForeignKey("parkings.parking_id"), nullable=False)
    id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    review= db.Column(db.Text, nullable=False)

    parking = db.relationship("Parking", backref="reviews")
    user = db.relationship("User", backref="reviews")

    def __repr__(self):
        return f"<Review review_id={self.review_id} review={self.review}\
             id={self.id} parking_id={self.parking_id} parking={self.parking} user={self.user}>"


def connect_to_db(flask_app, db_uri="postgresql:///onstreetparking", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == "__main__":
    from server import app

#     # Call connect_to_db(app, echo=False) if your program output gets
#     # too annoying; this will tell SQLAlchemy not to print out every
#     # query it executes.
    connect_to_db(app)
