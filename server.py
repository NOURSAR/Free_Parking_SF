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
    main_street= request.args.get('streetname')
    cross_street1=request.args.get('cross-street1')
    cross_street2=request.args.get('cross-street2')
    cross_streets = []
    list_of_objects=[]
    objects= Review.query.join(Parking).filter(Parking.st_name.contains(main_street) == True).all()
    # print(l)
    for object in objects:
        key= object.parking.st_name
        value =  object.review, object.parking.parking_id, [object.parking.latitude, object.parking.longtitude]
        # dd[key]= value
        creatObject= {key:value}
        list_of_objects.append(creatObject)
    print(list_of_objects, " HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
    if cross_street1 != "":
        cross_streets.append(cross_street1)
    if cross_street2 != "":
        cross_streets.append(cross_street2)
    cross_streets = sorted(cross_streets)
    # print(cross_streets, "LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
    # stname = Parking.query.filter_by(st_name=main_street).first()
    # main_street_filter = Parking.query.filter_by(st_name=search).all()
    # search_review=Review.query.join(Parking).filter_by(st_name=main_street).all()
    # print(search_review, "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    
    # for re in search_review: # working on review
    #     print(re.parking.st_name)
    #     print(re.parking.st_name, re.parking_id, re.review, "RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
    
    if len(cross_streets) == 0:
    # if not cross_street1 and not cross_street2:
        #then query for all parking objects that match st_name
        all_parkings_stname=Parking.query.filter(Parking.st_name.contains(main_street) == True).all()
        search_review=Review.query.join(Parking).filter(Parking.st_name.contains(main_street) == True).all()
    
        if all_parkings_stname:
            print("parking objects are in database")
            list_of_coords=[] 
            for street in all_parkings_stname:
                print(street)
                s=[street.latitude, street.longtitude]
                list_of_coords.append(s)

            return render_template('all_parkings.html',  list_of_coords= list_of_coords, all_parkings_stname=all_parkings_stname, search_review=search_review, list_of_objects=list_of_objects)
       
        else:
            flash("Parking is not in database. You can add to Database by submitting a parking space.")
            print("Parking is not in database")
            return render_template('add_parking.html')
    
    if len(cross_streets) == 1:
        flash("Please enter 2 cross streets or NO cross streets.")
        return render_template("search_parking.html")


    if len(cross_streets) == 2:
    # if cross_street1 and cross_street2:
        #then query for parking objects that match all three columns
        all_parkings_stname=Parking.query.filter_by(st_name=main_street, cross_st_1=cross_street1, cross_st_2=cross_street2).all()
        search_review=Review.query.join(Parking).filter_by(st_name=main_street).all()

        print(all_parkings_stname)
        if all_parkings_stname:
            print("parking objects are in database")
            list_of_coords=[] 
            for street in all_parkings_stname:
                print(street)
                s=[street.latitude, street.longtitude]
                list_of_coords.append(s)
            return render_template('all_parkings.html', list_of_coords=list_of_coords, all_parkings_stname = all_parkings_stname, search_review=search_review) 

        else:
            flash("Parking is not in database. You can add to Database by submitting a parking space.")
            print("Parking is not in database")
            return render_template('add_parking.html')
    
    

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
    # cross_streets = sorted(cross_streets)
    # print(cross_streets, "HAAAAAAAAAAAAAAAAAAAAAAAAAD")

    search_review=Review.query.join(Parking).filter_by(st_name = main_street).all()
    print(search_review, "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")

    
    all_parkings_coords = Parking.query.filter_by(latitude=lat, longtitude=lng).first()

    if all_parkings_coords != None: #checking if filtered lat and lng in database
        flash("parking spot already exists")
        print(" parking spot already exists")
        return render_template("add_parking.html")
    else: #if parking is not in database:
      print("parking is not in database") 
      if main_street == None:
        flash("Input should not be None")
        return render_template("add_parking.html")
      else:
        if "email" in session: #first we going to check if there is a user in session:
            print("user in session")
            parking = crud.create_parking(st_name=main_street, longtitude=lat, latitude=lng, cross_st_2=cross_street2, cross_st_1=cross_street1) #if user in session create the parking
            all_parkings_stname = Parking.query.filter_by(st_name=main_street).all() #filtering out all street names
            # print(all_parkings_stname, "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    
            list_of_coords=[]
            for parking in all_parkings_stname:
                # streets.append(street.st_name)
                s=[parking.latitude, parking.longtitude]
                list_of_coords.append(s)
                # streets.append(street.longtitude)
            print(list_of_coords)
            return render_template("all_parkings.html", list_of_coords=list_of_coords , all_parkings_stname=all_parkings_stname, search_review=search_review) #return all parkings with street name

        else: #if user not in session
            print("user not in session")
            # return render_template('login_page.html') either render template with login page 
            return redirect('/login-page') #or redirect to login page route

@app.route('/add-review', methods = ['GET', 'POST'])
def add_review():
    rev = request.form.get('rev')
    parking_id= request.form.get('parking_id')#returns None , I need to fix it: abetter way to get the st id
    # print("fffffffffffffffffffffffffffffffffffffffffffffffff", parking_id)
    print(parking_id)
    if parking_id == None:
        return redirect("/")
    else:
        parking= crud.get_parking_by_parking_id(parking_id)
        print(rev)
    
        email=session.get('email')
        user = crud.get_user_by_email(email)
        review = crud.create_review(rev, user, parking)
        if 'email' not in session:
            return redirect('/login-page')
    # variables in (all_parkings.html) are not recognized in this route. I need to fix them.
    # return  f" thank you for your review {review.review} , {parking_id}, {email}."
        else:
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
