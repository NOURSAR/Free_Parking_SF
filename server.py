from model import connect_to_db 
from model import User
from model import Parking
from model import Review
from flask import (Flask, render_template, request, flash, session, redirect)
import crud
import os
import requests 
import json
from jinja2 import StrictUndefined
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from flask_login import current_user



app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

app.secret_key = "NOR"

login_manager = LoginManager(app)
login_manager.login_view = '/login_page'
# @app.route("/review")
# def your_route():
#     return current_user.is_authenticated

@app.route('/')
def homepage():
    return render_template('search_parking.html')

@app.route('/search-parking')
def search_parking():
    main_street= request.args.get('streetname').capitalize()
    cross_street1=request.args.get('cross-street1')
    cross_street2=request.args.get('cross-street2')

    cross_streets = []
    if cross_street1 != "":
        cross_streets.append(cross_street1)
    if cross_street2 != "":
        cross_streets.append(cross_street2)
    cross_streets = sorted(cross_streets)
    
    if len(cross_streets) == 0:
    # if not cross_street1 and not cross_street2:
        #then query for all parking objects that match st_name
        all_parkings_stname=Parking.query.filter(Parking.st_name.contains(main_street) == True).all()
        # markers_reviews= Parking.query.filter(Parking.st_name.contains(main_street) == True).all()

        if all_parkings_stname:
            print("parking objects are in database")
            allofmarkers=[]
            for marker in all_parkings_stname:
                key = "street"
                marker_id =marker.parking_id
                coords=[marker.latitude, marker.longtitude]
                streetname=marker.st_name
                address= marker.address
                k=Review.query.join(Parking).filter(Parking.parking_id == marker_id).all()
                list_of_marker_reviews = ""
                for review in k:
                    if review.review == None:
                        review.review = "no review yet"
                        list_of_marker_reviews=list_of_marker_reviews+ review.review
                    else:
                        list_of_marker_reviews = list_of_marker_reviews+  "  -" +  review.review
                value= streetname, list_of_marker_reviews, marker_id, coords, address
                creatObject={key:value}
                allofmarkers.append(creatObject)
        
            return render_template('all_parkings.html',  all_parkings_stname=all_parkings_stname, allofmarkers=allofmarkers)
       
        else:
            if 'email' in session:
            # if id is not None:
              flash(id)
              flash("Parking is not in database. You can add to Database by submitting a parking spot.")
              print("Parking is not in database")
              return render_template('add_parking.html')
            else:
                flash("Parking is not in database. Login to add aparking spot")
                return redirect('/login-page')
    if len(cross_streets) == 1:
        flash("Please enter 2 cross streets or NO cross streets.")
        return render_template("search_parking.html")


    if len(cross_streets) == 2:
    # if cross_street1 and cross_street2:
        #then query for parking objects that match all three columns
        all_parkings_stname=Parking.query.filter_by(st_name=main_street, cross_st_1=cross_street1, cross_st_2=cross_street2).all()

        print(all_parkings_stname)
        if all_parkings_stname:
            print("parking objects are in database")
            allofmarkers=[]
            for marker in all_parkings_stname:
                key = "street"
                marker_id =marker.parking_id
                coords=[marker.latitude, marker.longtitude]
                streetname=marker.st_name
                address=marker.address
                k=Review.query.join(Parking).filter(Parking.parking_id == marker_id).all()
                list_of_marker_reviews = ""
                for review in k:
                    if review.review == None:
                        review.review = "-no review yet"
                    else:
                        list_of_marker_reviews = list_of_marker_reviews+  "  -" +  review.review
                value= streetname, list_of_marker_reviews, marker_id, coords, address 
                creatObject={key:value}
                allofmarkers.append(creatObject)
            return render_template('all_parkings.html', all_parkings_stname = all_parkings_stname, allofmarkers=allofmarkers) 

        else:
            if "email" not in session:
            # if id == None:
                print(id)
                flash("Parking is not in database, please log in to add parking spot")
                print("Parking is not in database")
                return redirect('/login-page')

            return render_template('add_parking.html')
            # return redirect('/login-page')
    
    

@app.route('/add-parking', methods = ['GET', 'POST'])
def add_parking():

    lat = request.form.get('lat') #get lat from from
    lng = request.form.get('lng') #get lng from form
    main_street = request.form.get('street') #get street from form
    cross_street1 = request.form.get('cross-street1')
    cross_street2 = request.form.get('cross-street2')
    address= request.form.get("address")
    print(address)
    cross_streets = []
    if cross_street1 != None:
        cross_streets.append(cross_street1)
    if cross_street2 != None:
        cross_streets.append(cross_street2)
    cross_streets = sorted(cross_streets)

  
    all_parkings_coords = Parking.query.filter_by(latitude=lat, longtitude=lng).first()

    if all_parkings_coords != None: #checking if filtered lat and lng in database
        flash("parking spot already exists")
        print(" parking spot already exists")
        return render_template("add_parking.html")
    else: #if parking is not in database:
      print("parking is not in database") 
      if main_street == None:
        flash("Please fill up the following form to submit a parking spot")
        return render_template("add_parking.html")
      else:
        if "email" in session: #first we going to check if there is a user in session:
            print("user in session")
            parking = crud.create_parking(st_name=main_street, longtitude=lat, latitude=lng, cross_st_2=cross_streets[0], cross_st_1=cross_streets[1], address=address) #if user in session create the parking
            all_parkings_stname=Parking.query.filter(Parking.st_name.contains(main_street) == True).all()
           # markers_reviews= Parking.query.filter(Parking.st_name.contains(main_street) == True).all()
        
            if all_parkings_stname:
                print("parking objects are in database")
                allofmarkers=[]
                for marker in all_parkings_stname:
                    key = "street"
                    marker_id =marker.parking_id
                    coords=[marker.latitude, marker.longtitude]
                    streetname=marker.st_name
                    address= marker.address
                    k=Review.query.join(Parking).filter(Parking.parking_id == marker_id).all()
                    list_of_marker_reviews = ""
                    for review in k:
                        if review.review == None:
                            # review.review = "-no review yet"
                            list_of_marker_reviews= "No review yet"
                        else:
                            list_of_marker_reviews = list_of_marker_reviews+  "  -" +  review.review
                    value= streetname, list_of_marker_reviews, marker_id, coords, address
                    creatObject={key:value}
                    allofmarkers.append(creatObject)
                return render_template("all_parkings.html",all_parkings_stname=all_parkings_stname, allofmarkers=allofmarkers, parking=parking) #return all parkings with street name

        else: #if user not in session
            print("user not in session")
            # return render_template('login_page.html') either render template with login page 
            return redirect('/login-page') #or redirect to login page route

@app.route('/add-review', methods = ['GET', 'POST'])
def add_review():
    rev = request.form.get('rev')
    parking_id= request.form.get('parking_id')
    print(parking_id)

    
    print(id)
    
    if parking_id == None:
        if rev== None:
           return redirect("/")
    else:
        parking= crud.get_parking_by_parking_id(parking_id)
        print(rev)
    
        email=session.get('email')
        user = crud.get_user_by_email(email)
        review = crud.create_review(rev, user, parking)
        return render_template('review_thankyou.html', review = review.review, email=email)
    #have review_thankyou.html thank user for review, show them review, add links giving user choice to add another parking spot/review or search again

@app.route('/login-page')
def login_page():
    """ Show login/create account page"""

    return render_template('login_page.html')


@login_manager.user_loader
def load_user(id):
    """ Flask-Login function to retrieve ID of user from session if any, and load user into memory """
    user = User.query.filter_by(id=id).first()
    
    return user
    

@app.route('/login', methods = ['GET', 'POST'])
def login():
    """ Log user in and add user info to session """

    if current_user.is_authenticated:
        return redirect('/')
        
    email = request.form.get('email')
    password = request.form.get('password')
    session['email'] = email    #adding user to the session
    user = crud.get_user_by_email(email)
    print("**********")
    print(user)
    print("**********")
    
    if user:
        if user.check_password(password)==True:
            login_user(user)
            flash('Login Successful')
            return redirect('/')
        else:
            flash('Invalid password.')
            return redirect('/login-page')
    else:
        flash('Sorry, this user does not exist.')
        return redirect('/login-page')


@app.route('/create-user', methods = ['POST'])
def create_login():
    """ Create login credentials for user """

    user_email = request.form.get('email')
    print(user_email)
  
    user_password = request.form.get('password')
    print(user_password)

    potential_user = crud.get_user_by_email(user_email)

    if potential_user != None:
        flash('Email already in use, please use a different email.')
        return redirect('/login-page')
    else:
        crud.create_user(email=user_email, password=user_password)
        flash('New account created! You may now log in.')
        return redirect('/login-page')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Successfully logged out')
    #session=None want to clear the session
    return redirect('/')



if __name__ == "__main__":
    connect_to_db(app)
    app.run(
        host="0.0.0.0",
        use_reloader=True,
        use_debugger=True,
    )

    # sudo pg_ctlcluster 13 main start
    # kill -9 $(ps -A | grep python | awk '{print $1}') 
