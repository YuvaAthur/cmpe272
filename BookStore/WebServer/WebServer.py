from app import app

# programmatic does not seem to work
# have to  $ . venv/bin/activate  | $ sudo bash to get access to port 80.
# better way is to use CLI :
#       $ flask run --host=0.0.0.0 --port=80
#if __name__ == '__main__':
#      app.run(host='0.0.0.0', port=80)