
from flask import Flask

app = Flask(__name__)
# app.run(debug=True)
# app.config.from_object('webapi.config') # from_pyfile('config.py')   # ('webapi.config') # 
app.secret_key = 'development key'

from . import routes
from . import forms
# from . import models
# from . import db_data



# # Model objects - include collection declarations
# from db import dbops

# # Forms
# from webapi.app import forms

# # # API Code
# from webapi.app import routes      

from context import db

# # # csrf =  forms.CSRFProtect(app)

# # #for JSON testing
# # import db_data




