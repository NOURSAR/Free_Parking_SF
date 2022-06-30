from model import db, Parking, User, Review, connect_to_db



def create_parking(st_name, longtitude, latitude, cross_st_1, cross_st_2, address):
    """ Create and return a parking"""

    cross_streets = sorted([cross_st_1, cross_st_2])
    cross_st1 = cross_streets[0]
    cross_st2 = cross_streets[1]
    
    parking= Parking(st_name=st_name, longtitude=longtitude,latitude=latitude, cross_st_1=cross_st1, cross_st_2=cross_st2, address=address)

    db.session.add(parking)
    db.session.commit()

    return parking


def create_review(review, user, parking):
    """Create a review"""

    review=Review(review=review, user=user, parking=parking)

    db.session.add(review)
    db.session.commit()

    return review


def show_all_parkings():
    "show all parkings"
    parkings= Parking.query.all()
    return parkings
def get_parking_by_parking_id(parking_id):
    """get parking by id"""
    parking_id= Parking.query.get(parking_id)
    return parking_id


def show_all_reviews():
    """show all reviews"""
    reviews = Review.query.all()
    return reviews


def create_user(email, password):
    """ Create and return a user """
    user = User(email=email, password_hash=password)

    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return user


def show_all_users():
    """ Return a list of all user objects """
    users = User.query.all()

    return users


def get_user_by_email(email):
    """ Query for user by email """
    user = User.query.filter_by(email=email).first()
    if user:
        return user
    else:
        return None


def get_user_by_id(id):
    """ Query for user by id """
    user = User.query.filter(id=id).first()

    return user

if __name__ == '__main__':
    from server import app
    connect_to_db(app)