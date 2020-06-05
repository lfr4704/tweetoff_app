# tweetoff_app/routes/tweet_routes.py

from flask import Blueprint, jsonify, request, render_template #, flash, redirect

from tweetoff_app.models import db, Tweet, parse_records

tweet_routes = Blueprint("tweet_routes", __name__)

@tweet_routes.route("/tweets.json")
def list_tweets():

    tweet_records = Tweet.query.all()
    print(tweet_records)
    tweets = parse_records(tweet_records)
    return jsonify(tweets)

@tweet_routes.route("/tweets")
def list_tweets_for_humans():

    tweet_records = Tweet.query.all()
    print(tweet_records)
    tweets = parse_records(tweet_records)
    return render_template("tweets.html", message="Here's some tweets", tweets=tweets)

@tweet_routes.route("/tweets/new")
def new_tweet():
    return render_template("new_tweet.html")

@tweet_routes.route("/tweets/create", methods=["POST"])
def create_tweet():
    print("FORM DATA:", dict(request.form))
    # todo: store in database
    new_tweet = Tweet(tweet=request.form["tweet_text"], user_id=request.form["tweeter_user"])
    db.session.add(new_tweet)
    db.session.commit()

    return jsonify({
        "message": "TWEET CREATED OK",
        "Tweet": dict(request.form)
    })
    #flash(f"Book '{new_book.title}' created successfully!", "success")
    #return redirect(f"/books")
