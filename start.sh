export FLASK_APP=src/app
flask run &
ngrok http http://127.0.0.1:5000/
