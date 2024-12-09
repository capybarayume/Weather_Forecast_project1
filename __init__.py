from flask import Flask, Blueprint
from flask_session import Session

def create_app():
    app=Flask(__name__)
    #write your own secret key
    app.config["SECRET_KEY"]="000000000"

    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"

    Session(app)

    from views import views as viewsbp
    app.register_blueprint(viewsbp,url_prefix="/")

    @app.after_request
    def after_request(response):
        """Ensure responses aren't cached"""
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response


    return app