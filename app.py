<<<<<<< HEAD
# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request)

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db/db.sqlite"

db = SQLAlchemy(app)

class Gis(db.Model):
    __tablename__ = 'gisdata'

    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.String(64))
    longitude = db.Column(db.String(64))
    altitude = db.Column(db.String(64))
    time = db.Column(db.String(64))

    def __repr__(self):
        return '<Gis %r>' % (self.latitude)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        latitude = request.form["info_cur_lat"]
        longitude = request.form["info_cur_lng"]
        altitude = request.form["info_cur_alt"]
        time = request.form["info_cur_tm"]

        location = Gis(latitude=latitude, longitude=longitude, altitude=altitude, time=time)
        db.session.add(location)
        db.session.commit()

        return "Receive data"


@app.route("/api/data")
def list_locations():
    results = db.session.query(Gis.latitude, Gis.longitude, Gis.altitude, Gis.time).all()

    locations = []
    for result in results:
        locations.append({
            "latitude": result[0],
            "longitude": result[1],
            "altitude": result[2],
            "time": result[3]
        })
    return jsonify(locations)


if __name__ == "__main__":
   app.run(debug=True)
=======
# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
   
    request)

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db/db.sqlite"

db = SQLAlchemy(app)


class Gis(db.Model):
    __tablename__ = 'gisdata'

    id = db.Column(db.Integer, primary_key=True)
<<<<<<< HEAD
    latitude = db.Column(db.String(64))
    longitude = db.Column(db.String(64))
    altitude = db.Column(db.String(64))
    time = db.Column(db.String(64))

    def __repr__(self):
        return '<Gis %r>' % (self.latitude)


=======
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    altitude = db.Column(db.Float)
    time = db.Column(db.String(64))

    def __repr__(self):
        return '<Gis %r>'


@app.before_first_request
def setup():
    # Recreate database each time
    db.drop_all()
    db.create_all()


>>>>>>> 200f81a0dcf19faed3788fb9fa44cd0756e789cf
# request.home['']
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
<<<<<<< HEAD
        latitude = request.form["info_cur_lat"]
        longitude = request.form["info_cur_lng"]
        altitude = request.form["info_cur_alt"]
        time = request.form["info_cur_tm"]

        location = Gis(latitude=latitude, longitude=longitude, altitude=altitude, time=time)
=======
        latitude = request.home["info_cur_lat"]
        longitude = request.home["info_cur_lng"]
        altitude = request.home["info_cur_alt"]
        time = request.home["info_cur_tm"]

        location = location(latitude=latitude, longitude=longitude, altitude=altitude, time=time)
>>>>>>> 200f81a0dcf19faed3788fb9fa44cd0756e789cf
        db.session.add(location)
        db.session.commit()

        return "Receive data"
<<<<<<< HEAD
=======

    return render_template("home.html")


>>>>>>> 200f81a0dcf19faed3788fb9fa44cd0756e789cf

        

@app.route("/api/data")
def list_locations():
    results = db.session.query(Gis.latitude, Gis.longitude, Gis.altitude, Gis.time).all()

    locations = []
    for result in results:
<<<<<<< HEAD
        locations.append({
=======
        locationss.append({
>>>>>>> 200f81a0dcf19faed3788fb9fa44cd0756e789cf
            "latitude": result[0],
            "longitude": result[1],
            "altitude": result[2],
            "time": result[3]
        })
    return jsonify(locations)





if __name__ == "__main__":
   app.run(debug=True)
>>>>>>> 1056e04fbbd0eda6aacac4cbf6872cf904cffaea
