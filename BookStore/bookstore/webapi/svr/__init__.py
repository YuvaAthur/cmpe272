from flask import Flask

app = Flask(__name__)
# app.run(debug=True)
# app.config.from_object('webapi.config') # from_pyfile('config.py')   # ('webapi.config') # 
app.secret_key = 'development key'

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






