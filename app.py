from flask import Flask, render_template, redirect, request, session
import os
from oauth import Oauth

app = Flask(__name__)
app.config["SECRET_KEY"] ="347834y7tureiwfhbjvfwkehuiergy"


@app.route('/')
def home():
    return render_template("index.html", discord_url=Oauth.discord_login_url)


@app.route('/invite')
def invite():
    return render_template("invite.html")


@app.route('/privacy')
def terms():
    return render_template("privacy.html")

 
@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/login')
def login():
    code = request.args.get("code")
    at = Oauth.get_access_token(code)
    session["token"] = at

    user = Oauth.get_user_json(at)
    user_name, user_discrim, user_avatar, user_id = user.get("username"), user.get("discriminator"), user.get("avatar"), user.get("id")
    user_avatar_url = f"https://cdn.discordapp.com/avatars/{user_id}/{user_avatar}.png"
    user_discrim = str(user_discrim)
    userName = user_name + "#" + user_discrim
    print(userName)
    return render_template('dashboard.html', user_avatar_url=user_avatar_url, user_tag=userName)


@app.errorhandler(404)
def page_no_found(e):
    return render_template("404.html"), 404
