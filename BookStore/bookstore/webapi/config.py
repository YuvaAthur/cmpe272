# SECRET_KEY = "powerful secretkey"

import os
#class Config(object): # for some reason this class is not fully visible :(!

# Flask runtime configuration
DEBUG = True # Turns on debugging features in Flask
BCRYPT_LOG_ROUNDS = 12 # Configuration for the Flask-Bcrypt extension
MAIL_FROM_EMAIL = "yuva.athur@sjsu.edu" # For use in application emails

# For webforms
SECRET_KEY = "powerful secretkey"
# WTF_CSRF_SECRET_KEY = "a csrf secret key"
#SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
