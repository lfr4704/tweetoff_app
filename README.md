# tweetoff_app
Predictive model app for tweets from two different users using twitter api

# Installation

# Setup

```sh
pipenv --python 3.7
```

```sh
pipenv install Flask Flask-SQLAlchemy Flask-Migrate
```

#activate virtual environment

```sh
pipenv shell
```

Migrate the database:

```sh
FLASK_APP=tweetoff_app flask db init
FLASK_APP=tweetoff_app flask db migrate
FLASK_APP=tweetoff_app flask db upgrade
```

# Usage

```sh
FLASK_APP=tweetoff_app flask run
```
