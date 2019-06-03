from flask import *
import os
from sqlalchemy import create_engine
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')
db = create_engine('postgres://npdvxwlrbkcwbk:02f49f9101fd6e9ed966c25f7ff3836e3644639e5a01a910dd92e7caa62a62fd@ec2-107-20-230-70.compute-1.amazonaws.com:5432/daqbaoap2pkdsk')
# db.execute("CREATE TABLE users (id int, username varchar(255), password varchar(255))")
# db.execute("CREATE TABLE survey (id int, username varchar(255), q1 varchar(255), q2 varchar(255), q3 varchar(255))")

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("login")
        return f(*args, **kwargs)
    return decorated_function

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    # Ensure that inputted username/password forms are filled
    if request.method == "POST":
        if not request.form.get("email"):
            return

        elif not request.form.get("password"):
            return

        # Fetch information from database
        rows = db.execute("SELECT * FROM users WHERE email = '%s'" % (request.form.get("email")))
        fetch = rows.fetchall()

        # If fetch does not return information, or if the passwords are incorrect, return user to login screen
        if not fetch or not check_password_hash(fetch[0]["password"], request.form.get("password")):
            return

        # Assign user_id for each session
        session["user_id"] = request.form.get("email")

        # Direct user to predict page upon successful login
        return redirect("/")
    return

@app.route("/register", methods=["GET", "POST"])
def register():
    # Ensure username, password, and confirmation forms are filled
    if request.method == "POST":
        if not request.form.get("email"):
            return redirect("register")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return redirect("/register")

        elif not request.form.get("confirmPassword"):
            return redirect("/register")

        # Define username and password, hashing password
        username = request.form.get("email")
        password = generate_password_hash(request.form.get("password"))

        # Query database for username
        try:
            rows = db.execute("SELECT * FROM users WHERE email = ('%s')" % (email))
            fetch = rows.fetchall()
            if len(fetch) >= 1:
                return redirect("/register")
        except:
        	pass

        # Ensure password and confirmation password are the same
        if request.form.get("password") != request.form.get("confirmPassword"):
            return redirect("/register")
        # Insert new user into users
        db.execute("INSERT INTO users (email, password) VALUES ('%s', '%s')" % (email, password))
        return redirect("login")
    return 

@votr.route('/user/<email>')
def api_user(email):
    user = Topics.query.filter(Topics.title.like(api_user)).first()
    return jsonify({'User': [user.to_json()]}) if user else jsonify({'message': 'user not found'})

@app.route('/test', methods = ['GET'])
def test():
	return '<h1>Deployed</h1>'

@app.route("/logout")
@login_required
def logout():
    # Implementation of logout button
    session.clear()
    return redirect("/")


if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')