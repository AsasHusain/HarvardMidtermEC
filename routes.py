from flask import Flask, flash, render_template, request, url_for, redirect, jsonify, session
# import Flask, flash, render_template, request, url_for, redirect, jsonify, session from flask
from models import db, User, Condo
from forms import LoginForm, SignupForm
# sha256_crypt from passlib.hash

#from flask_heroku import Heroku

app = Flask(__name__)
app.secret_key = "cscie14a-midterm"

# local postgresql or heroku postgresql 

db_session = db('localhost','postgres','admin')



# index route

# signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():

    print(request.form)
    form = SignupForm(request.form)
    
    if request.method == 'POST':
        user = User()
        
        user.init(form.username.data, form.password.data)
        print(form.username.data,"|",form.password.data," DIRECT")
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)
# login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        u = User()
        u.init(request.form['username'],request.form['password'])
        val = db_session.validate(u)
        #if request.form['username'] != 'admin' or request.form['password'] != 'admin':
        if not val:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)
# logout route

@app.route('/home', methods=['GET', 'POST'])
def home():
    error = None
    c = Condo(db_session)
    total = c.get_total()
    return render_template('index.html', error=error, total=total)



# info route
@app.route('/info/<mlsnum>')
def info(mlsnum):
    c = Condo(db_session)
    listing = c.get_details(mlsnum)
    print(listing)
    # round listing prices
    #listing.ppsf = '{0:.2f}'.format(listing.ppsf)
    #listing.list_price = '{0:.2f}'.format(listing.list_price)
    #listing.predicted_price = '{0:.2f}'.format(listing.predicted_price)
    return render_template('info.html', mls=listing[7], url=listing[4], sqft=listing[3], beds=listing[2], baths=listing[6],\
                            ppsf=listing[5],rmks=listing[9],lp=listing[8],pp=listing[10])
# add the rest of the info route here


# load_data route (for D3 vis)

if __name__ == "__main__":
    app.run(debug=True)
