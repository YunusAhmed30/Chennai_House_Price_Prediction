import json
import numpy as np
import pickle


__locations=None
__data_columns=None
__model=None

def get_location_names():
    return __locations

def get_estimated_price(location,sqft,n_rooms,n_bedrooms,n_bathrooms):
    try:
        loc_index = __locations.index(location.lower())
    except:
        return -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = n_rooms
    x[2] = n_bedrooms
    x[3] = n_bathrooms

    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)

def load_saved_artifacts():
    print('Loading saved artifacts')
    global __locations
    global __data_columns
    global __model

    with open("./artifacts/Columns_chennai1.json",'r') as f:
        __data_columns=json.load(f)['data_columns']
        __locations=__data_columns[11:17]

    with open("./artifacts/Chennai_house_prices.pickle",'rb') as f:
        __model=pickle.load(f)

if __name__=="__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('AREA_Karapakkam',1500,4,2,1))