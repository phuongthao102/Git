from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import cloudinary

app = Flask(__name__)
app.secret_key = 'hghgffugygbfdgjhghjghfgffcghghjtftvhjij(&*&&*OHH&*%&*gtyffgfrtđyguhjhhiu'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/me?charset=utf8mb4" % quote('Admin@123')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 12

db = SQLAlchemy(app=app)
login = LoginManager(app=app)

cloudinary.config(
    cloud_name="dyoffqmct",
    api_key="238459722644888",
    api_secret="9nfm1jYmP1Cybitg-GaQyroKGzA",
    secure=True
)
