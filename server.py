# from cgitb import html, text
# from crypt import methods
# from tokenize import Name
# from webbrowser import get
from jinja2 import StrictUndefined
import model
from model import Parking, Coordinate
import pprint

from flask import (Flask, render_template, request, flash, session, redirect)
# from model import connect_to_db, db
import json
import crud
import pprint
import requests
# os.system('dropdb onstreetparking')

# os.system('createdb onstreetparking')
# os.system('dropdb onstreetparking')


# model.connect_to_db(server.app)
# model.db.create_all()

app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

app.secret_key = "NOR"
@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/search')
def search():
    street_name= request.args.get("street_name").upper()
    filter = Parking.query.filter_by(st_name=street_name).first()
    parkings_in_db=[]
    if filter is not None:
        print(street_name, "is in database")
    else:
        payload={"st_name": street_name}
        response = requests.get('https://data.sfgov.org/resource/9ivs-nf5y.json?', params=payload)
        res=response.json()
        pprint.pprint("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL", res)
        print(street_name, "is not in database")
        for parking in res:
            st_name, cnn, st_type, district, prkg_sply, collectn, year =(
                parking["st_name"],
                parking["cnn"],
                parking["st_type"],
                parking["district"],
                parking["prkg_sply"],
                parking["collectn"],
                parking["year"],
            )
            db_parking = crud.create_parking(st_name, cnn, st_type, district, prkg_sply, collectn, year)
            for lonlat in parking["shape"]["coordinates"]:
                lon, lat =( 
                lonlat[0],
                lonlat[1],
                )
                db_lonlat=crud.create_coordinate(lon, lat, db_parking) ##will append all coordinates that belong to the same street to it
                parkings_in_db.append(db_lonlat)
        model.db.session.add_all(parkings_in_db)
        model.db.session.commit()
    filter = Parking.query.filter_by(st_name=street_name).all()
    coordinates = [parking_spot.coordinates for parking_spot in filter]
    myLatLng =[]
    for coordinate in coordinates: 
        for spot in coordinate:
            # print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL", spot.lat)
            latLng=[spot.lat, spot.lon]
            myLatLng.append(latLng)
    print(myLatLng)

    return render_template("all_parkings.html", parkings=filter, coordinates=coordinates, myLatLng=myLatLng)
           
@app.route("/parkings")
def all_parkings():
    """View all parkings."""
    parkings = crud.get_parkings()
    coordinates= crud.get_coordinates()
    return render_template("all_parkings.html", parkings=parkings, coordinates=coordinates)

@app.route("/coordinates")
def all_coordinates():
    """View all coordinates."""
    parkings = crud.get_parkings()
    coordinates= crud.get_coordinates()
    return render_template("all_parkings.html", coordinates=coordinates, parkings=parkings, )

@app.route("/parkings/<parking_id>")
def show_parking(parking_id):
    """Show details on a particular parking."""

    parking = crud.get_parking_by_id(parking_id)
    coordinate= crud.get_parking_coordinates(parking_id)

    return render_template("parking_details.html", parking=parking, coordinate=coordinate)

# @app.route("/coordinates/<parking_id>")
# def show_parking(parking_id):
#     """Show details on a particular parking."""

#     coordinate= crud.get_parking_coordinates(parking_id)
#     return render_template("parking_details.html", coordinate=coordinate)



if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        use_reloader=True,
        use_debugger=True,
    )

    # kill -9 $(ps -A | grep python | awk '{print $1}')
