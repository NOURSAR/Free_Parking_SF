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
    return render_template('homepage.html')

@app.route('/search-parking')
def search_parking():
    search= request.form.get('search')

    stname = Parking.query.filter_by(st_name=search).all()

    if stname is not None:
        print("parking is in database")
        return render_template('all_parkings.html') 

    return redirect('/add-parking')

@app.route('/add-parking', methods = ['GET', 'POST'])
def add_parking():
    lat= request.form.get('lat')
    lng= request.form.get('lng')
    st_name= request.form.get('street')

    # filter1 = Parking.query.filter_by(st_name=st_name).all()
    filter2 = Parking.query.filter_by(longtitude=lng).first()
    filter3 = Parking.query.filter_by(latitude=lat).first()
    if filter2 and filter3 is not None:
        print(" parkinig spot already exists")
        return render_template("all_parkings.html")
    else: 
        print("parking is not in database")
        print(lat, lng, st_name)
        if "email" in session:
            parking = crud.create_parking(st_name=st_name, longtitude=lat, latitude=lng)
            print(parking.st_name)
            return  f"{lat} {lng} {st_name}" #temporary
            # return redirect("/add-review")
        else:
           return render_template('login_page.html')
# @app.route('/add-review', methods = ['GET', 'POST'])
# def add_review():
#     # user = crud.get_user_by_id(id)
#     # parking= crud.get_parking_by_parking_id(parking_id)

#     rev = request.form.get('rev')
#     print(rev)
#     # user=crud.get_user_by_id(user.id)
#     # print(user)
#     # parking=crud.get_parking_by_parking_id(parking_id)
#     # print(parking)
#     if "user" == None:
#         return redirect('/login-page')
    
    # review = crud.create_review(review=rev)
    # print(review)
    # return f"{review}"
    
    # return  f"{rev} {review}"

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
            # flash('Login Successful')
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
    return redirect('/')



if __name__ == "__main__":
    connect_to_db(app)
    app.run(
        host="0.0.0.0",
        use_reloader=True,
        use_debugger=True,
    )

    
    # kill -9 $(ps -A | grep python | awk '{print $1}')
