from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
# connection string (host name, user id, password, database name)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://vos_api:Butt3rfly!@localhost:5432/VOS'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

VOSDb = SQLAlchemy(app)