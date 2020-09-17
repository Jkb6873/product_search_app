# if no virtualenv, create virtualenv
[ ! -d venv ] && virtualenv venv

# source virtualenv
source venv/bin/activate

# install packages
pip install -r requirements.txt

export FLASK_APP=app.py

if [[ $1 == "test" ]]; then
  #run tests
  python -m unittest
else
  #start server
  python -m flask run
fi
