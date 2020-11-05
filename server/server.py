from flask import Flask,request,jsonify
import util

app=Flask(__name__)

@app.route("/get_location_names")
def get_location_names():
    response=jsonify({
        'location':util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route("/get_estimated_price",methods=['POST'])
def get_estimated_price():
    sqft = float(request.form['sqft'])
    location = request.form['location']
    n_rooms = request.form['n_rooms']
    n_bedrooms = request.form['n_bedrooms']
    n_bathrooms = request.form['n_bathrooms']

    response=jsonify({
        'estimated_price':util.get_estimated_price(location,sqft,n_rooms,n_bedrooms,n_bathrooms)
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__=="__main__":
    util.load_saved_artifacts()
    print('Starting Flask server..')
    app.run()