from flask import Flask, render_template, g, redirect, url_for


app = Flask(__name__)

# for Okta
from flask_oidc import OpenIDConnect
from okta import UsersClient

# authorization usig Okta
app.config["OIDC_CLIENT_SECRETS"] = "client_secrets.json"
app.config["OIDC_COOKIE_SECURE"] = False
app.config["OIDC_CALLBACK_ROUTE"] = "/oidc/callback"
app.config["OIDC_SCOPES"] = ["openid", "email", "profile"]
app.config["SECRET_KEY"] = "hello123"
app.config["OIDC_ID_TOKEN_COOKIE_NAME"] = "oidc_token"
oidc = OpenIDConnect(app)
okta_client = UsersClient("https://dev-833144.okta.com", "00xJ6vTQkI8LzIQcPXf7Ehw75GrdAVDdqA2tvQFxFx")



# app = Flask(__name__)
# # app.run(debug=True)
# # app.config.from_object('webapi.config') # from_pyfile('config.py')   # ('webapi.config') # 
# app.secret_key = 'development key'

from . import routes
from . import forms
from . import models
from db.data import sample_data # for local tests



# # Model objects - include collection declarations
# from db import dbops

# # Forms
# from webapi.app import forms

# # # API Code
# from webapi.app import routes      

from context import db

# # # csrf =  forms.CSRFProtect(app)






