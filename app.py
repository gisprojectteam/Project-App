# import necessary libraries
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
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    altitude = db.Column(db.Float)
    time = db.Column(db.String(64))

    def __repr__(self):
        return '<Gis %r>


@app.before_first_request
def setup():
    # Recreate database each time
    db.drop_all()
    db.create_all()


# request.home['']
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        latitude = request.home["info_cur_lat"]
        longitude = request.home["info_cur_lng"]
        altitude = request.home["info_cur_alt"]
        time = request.home["info_cur_tm"]

        location = location(latitude=latitude, longitude=longitude, altitude=altitude, time=time)
        db.session.add(location)
        db.session.commit()

        return "Receive data"

    return render_template("home.html")




@app.route("/api/data")
def list_locations():
    results = db.session.query(Gis.latitude, Gis.longitude, Gis.altitude, Gis.time).all()

    locations = []
    for result in results:
        locationss.append({
            "latitude": result[0],
            "longitude": result[1],
            "altitude": result[2],
            "time": result[3]
        })
    return jsonify(locations)





if __name__ == "__main__":
    app.run()
