#from app import app, db
#from app.views import recommendation_views
from flask import Flask
from flask_cors import CORS, cross_origin
import os
#from app.models import *


# Define WSGI app object
app = Flask(__name__)
uri = os.environ['DATABASE_URL']
#app.config["SQLALCHEMY_DATABASE_URI"] = uri
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(app)
CORS(app)

# https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications
# if __name__ == "__main__":
#   app.run(host='0.0.0.0', port=8081, debug=True)
# recommendation_views = Blueprint("recommendation_views", __name__, url_prefix="/api/v1/")
# app.register_blueprint(recommendation_views)

@app.route("/recommendations", methods=["GET"])
def get_recommendations():
  print("hello")
  movies = list()
  movie = {
    "movie_id": 1,
    "title": "Test Movie",
    "artists": list(),
    "ranking": 1
  }
  movies.append(movie)
  response = {
    "movies": movies
  }
  return jsonify(response)
  #page = request.args.get('page', default=1)
  #page_int = int(page)
  #items = request.args.get('items', default=4)
  #items_int = int(items)
  #item_end = page_int * items_int
  #item_start = item_end - items_int

  ## count of times movie recommended grouped by movie id
  #sorted_rec_by_movie = db.session.query(
  #  Recommendation.movie_id,
  #  Movie.title,
  #  db.func.count(Recommendation.id)
  #).outerjoin(Movie, Recommendation.movie_id == Movie.id)\
  #  .group_by(Recommendation.movie_id, Movie.title)\
  #  .order_by(db.func.count(Recommendation.movie_id)\
  #  .desc()).all()

  #resp = {
  #  "results_length": len(sorted_rec_by_movie),
  #  "movies": list()
  #}

  #splice = sorted_rec_by_movie[item_start:item_end]

  ## sort by highest to lowest
  #for idx, rec in enumerate(splice):
  #  if idx < int(items):
  #    recs_per_movie = Recommendation.query.filter_by(movie_id = rec.movie_id).all()
  #    movie = {
  #      "movie_id": rec.movie_id,
  #      "title": rec.title,
  #      "artists": list(),
  #      "ranking": item_start + idx + 1
  #    }

  #    for recpm in recs_per_movie:
  #      artist = {
  #        "artist_name": recpm.artist.name,
  #        "source_link": recpm.source.source_link,
  #        "source_name": recpm.source.source_short_name
  #      }

  #      movie["artists"].append(artist)

  #    resp["movies"].append(movie)

  #resp = jsonify(resp)
  #return resp
