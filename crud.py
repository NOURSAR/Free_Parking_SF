from model import db, Parking, Coordinate ,connect_to_db
# import pandas as pd
# from sodapy import Socrata
# import pprint
# import requests

def create_parking(st_name, cnn, st_type, district, prkg_sply, collectn, year):
    """Create and return a parking."""

    parking = Parking(st_name=st_name, cnn=cnn, st_type=st_type, district=district, prkg_sply=prkg_sply, collectn=collectn, year=year)

    return parking
    
def create_coordinate(lat, lon, parking):
    """Create and return parking."""

    coordinates = Coordinate(lat=lat, lon=lon, parking=parking)

    return coordinates

def get_parkings():
    """return all parkings"""
    return Parking.query.all()

def get_coordinates():
    """return all coordinates"""
    return Coordinate.query.all()

def get_parking_by_id(parking_id):
    """get parking by id"""
    return Parking.query.get(parking_id)

def get_parking_coordinates(parking_id):
    """get coordinates for a parking"""
    return Coordinate.query.join(Parking).filter(Coordinate.parking_id== parking_id).all()

# client = Socrata("data.sfgov.org", None)
# results_street = client.get("9ivs-nf5y", limit=2000)
# results_df_st = pd.DataFrame.from_records(results_street)
# pprint.pprint(results_street)
# pprint.pprint(results_df_st)
# payload ={'st_name':"'01ST'"}
# results_regulatuion = client.get("hi6h-neyh", limit=2000)
# results_df_reg = pd.DataFrame.from_records(results_regulatuion)
# pprint.pprint(results_regulatuion)
# pprint.pprint(results_df_reg)

# results_sweep = client.get("yhqp-riqs", limit=2000)
# results_df_sweep = pd.DataFrame.from_records(results_sweep)

# pprint.pprint(results_sweep)
# pprint.pprint(results_df_sweep)
# st_name='01ST'
# payload ={'st_name': '01ST'}

# response = requests.get('https://data.sfgov.org/resource/9ivs-nf5y.json', params=payload)
# res= response.json()
# pprint.pprint(res[1])
# response1 = requests.post('https://data.sfgov.org/resource/9ivs-nf5y.json', data=payload) //needs token

# pprint.pprint(response.jSon())



# if __name__ == '__main__':
#     from server import app
#     connect_to_db(app)