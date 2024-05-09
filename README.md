Clone this repository using: git clone https://github.com/zerg959/flask-web-app.git
Optional: Go to the project root directory and install the virtualenv library using pip and create a virtual environment. Run the following commands respectively:
pip install virtualenv
virtualenv venv
source venv/bin/activate
Download and install all dependencies in the requirements.txt using pip install -r requirements.txt
Start Flask’s built-in web server: $ flask run
Open your browser and view the app by opening the link http://127.0.0.1:5000/
To change port reun: flask run -h localhost -p 3000
You are free to view recent posts, register, login add new posts etc.
To reinitialize sample database run $ python init_db.py from tmp folder.