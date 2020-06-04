
#tweetoff_app/__init__.py

from flask import Flask

#from tweetoff_app.models import db, migrate
from tweetoff_app.routes.home_routes import home_routes
from tweetoff_app.routes.tweet_routes import tweet_routes

#DATABASE_URI = "sqlite:///tweetoff_app.db"

def create_app():
    app = Flask(__name__)

    # app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    # db.init_app(app)
    # migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    app.register_blueprint(tweet_routes)
    return init_app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
