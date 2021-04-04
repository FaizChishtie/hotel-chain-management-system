import os
from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_table import Table, Col
from flask_sqlalchemy  import SQLAlchemy
from flask_migrate import Migrate


# from src.db.database import User
from __init__ import CURRENT_USER, USERNAME, PASSWORD, DATA, HEADER
from src.forms.forms import LoginForm, RecordForm, CustomerProfileForm, EmployeeProfileForm, AddHotelForm, AddHotelChainForm, RecordForm, SearchForm
from src.util.util import profile_is_set
from src.db.User import User

######## HARDCODED ########

LOGIN_ = {'admin':'admin12345' , 'employee': 'employee123', 'customer': 'customer123'}

######## HARDCODED ########


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
# app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{USERNAME}:{PASSWORD}@web0.eecs.uottawa.ca:15432/group_a01_g44'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

######## ROUTES ########

def logged_in():
    global CURRENT_USER
    if not CURRENT_USER:
        flash('Please login!')
        return False
    return True

######## INDEX ########

@app.route('/')
@app.route('/index')
def index():
    global CURRENT_USER
    print(CURRENT_USER)
    if not logged_in():
        return redirect(url_for('login'))

    # if not profile_is_set(current_user):
    #     flash('Please set up your profile before continuing with the system!')
    #     return redirect(url_for('student_profile'))
    return render_template('index.html', data=CURRENT_USER)

######## INDEX ########


######## ROUTES ########

######## LOGIN/SIGNUP ########

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        username = form.username.data
        password = form.password.data

        if username and password:
            if username in list(LOGIN_.keys()):
                if LOGIN_[username] == password:
                    global CURRENT_USER
                    # AUTH
                    if username == 'admin':
                        CURRENT_USER = User(username, 'Admin')
                    if username == 'employee':
                        CURRENT_USER = User(username, 'Employee')
                    if username == 'customer':
                        CURRENT_USER = User(username, 'Customer')
                    flash(f'Authenticated as {username}')
                    return redirect(url_for('index'))
        
        flash('Invalid username or password')

    return render_template('login.html', form=form)


######## ADMIN ########

@app.route('/add_hotel', methods=['GET', 'POST'])
def add_hotel():
    global CURRENT_USER
    if not logged_in():
        return redirect(url_for('login'))
    elif not CURRENT_USER.isAdmin():
        flash(f'Unable to access page while logged in as {CURRENT_USER.type}')
        return redirect(url_for('index'))

    form = AddHotelForm()

    if form.validate_on_submit():
        print('TODO')
    
    return render_template('add_hotel.html', form=form)

@app.route('/add_hotelchain', methods=['GET', 'POST'])
def add_hotelchain():
    global CURRENT_USER
    if not logged_in():
        return redirect(url_for('login'))
    elif not CURRENT_USER.isAdmin():
        flash(f'Unable to access page while logged in as {CURRENT_USER.type}')
        return redirect(url_for('index'))

    form = AddHotelChainForm()

    if form.validate_on_submit():
        print('TODO')

    return render_template('add_hotelchain.html', form=form)

@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    global CURRENT_USER
    if not logged_in():
        return redirect(url_for('login'))
    elif not CURRENT_USER.isAdmin():
        flash(f'Unable to access page while logged in as {CURRENT_USER.type}')
        return redirect(url_for('index'))

    form = CustomerProfileForm()

    if form.validate_on_submit():
        print('TODO')

    return render_template('add_customer.html', form=form)

@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    global CURRENT_USER
    if not logged_in():
        return redirect(url_for('login'))
    elif not CURRENT_USER.isAdmin():
        flash(f'Unable to access page while logged in as {CURRENT_USER.type}')
        return redirect(url_for('index'))

    form = EmployeeProfileForm()

    if form.validate_on_submit():
        print('TODO')

    return render_template('add_employee.html', form=form)

@app.route('/add_record', methods=['GET', 'POST'])
def add_record():
    global CURRENT_USER
    if not logged_in():
        return redirect(url_for('login'))
    elif CURRENT_USER.isCustomer():
        flash(f'Unable to access page while logged in as {CURRENT_USER.type}')
        return redirect(url_for('index'))

    form = RecordForm()

    if form.validate_on_submit():
        print('TODO')
    
    return render_template('add_record.html', form=form)

@app.route('/search', methods=['GET', 'POST'])
def search():
    global CURRENT_USER
    if not logged_in():
        return redirect(url_for('login'))

    form = SearchForm()

    if form.validate_on_submit():
        global DATA
        global HEADER

        DATA = [['temp']]
        HEADER = ['hi']

        return redirect(url_for('results'))

        constraints = []

        if form.rid.data:
            # (rid,hid,csin,price,roomcapacity,amenities,rview,isextendable)
            constraints.append(f'rid = {form.rid.data}')
        if form.room_view.data:
            # (rid,hid,csin,price,roomcapacity,amenities,rview,isextendable)
            constraints.append(f'rview = {form.room_view.data}')
        if form.amenities.data:
            constraints.append(f'amenities = {form.amenities.data}')
        if form.price.data:
            constraints.append(f'price = {form.price.data}')
        if form.n_occupants.data:
            constraints.append(f'roomcapacity = {form.n_occupants.data}')

        if len(constraints) != 0:
            constraint = ""
            for i in range(len(constraints)):
                if i == (len(constraints) - 1):
                    constraint += constraints[i]
                else:
                    constraint += constraints[i] + " AND "
            print(constraint)
            DATA = db_get_all_items_with_constraints('room', constraint)


        else :
            DATA = db_get_all_items('room')
        HEADER = ['Room ID', 'Hotel ID', 'Price', 'Capacity', 'Amenities', 'View', 'Is Extendable']

        return redirect(url_for('results'))
    
    return render_template('search.html', form=form)

@app.route('/results')
def results():
    global CURRENT_USER
    global DATA
    global HEADER
    if not logged_in():
        return redirect(url_for('login'))
    return render_template('results.html', data=DATA, header=HEADER)

@app.route('/view_all_customers')
def view_all_customers():
    global CURRENT_USER
    if not logged_in():
        return redirect(url_for('login'))
    elif not CURRENT_USER.isAdmin():
        flash(f'Unable to access page while logged in as {CURRENT_USER.type}')
        return redirect(url_for('index'))
    return render_template('view_all_customers.html', data=db_get_all_items('customer'))

@app.route('/view_all_employees')
def view_all_employees():
    global CURRENT_USER
    if not logged_in():
        return redirect(url_for('login'))
    elif not CURRENT_USER.isAdmin():
        flash(f'Unable to access page while logged in as {CURRENT_USER.type}')
        return redirect(url_for('index'))
    return render_template('view_all_employees.html', data=db_get_all_items('employee'))

@app.route('/view_hotels')
def view_hotels():
    global CURRENT_USER
    if not logged_in():
        return redirect(url_for('login'))
    elif not CURRENT_USER.isAdmin():
        flash(f'Unable to access page while logged in as {CURRENT_USER.type}')
        return redirect(url_for('index'))
    return render_template('view_hotels.html', data=db_get_all_items('hotel'))

@app.route('/view_records')
def view_records():
    global CURRENT_USER
    if not logged_in():
        return redirect(url_for('login'))
    elif not CURRENT_USER.isAdmin():
        flash(f'Unable to access page while logged in as {CURRENT_USER.type}')
        return redirect(url_for('index'))
    return render_template('view_records.html', data=db_get_all_items('record'))

@app.route('/view_room')
def view_room():
    global CURRENT_USER
    if not logged_in():
        return redirect(url_for('login'))
    elif not CURRENT_USER.isAdmin():
        flash(f'Unable to access page while logged in as {CURRENT_USER.type}')
        return redirect(url_for('index'))
    return render_template('view_room.html', data=db_get_all_items('room'))


def as_cursor(query):
    connection = db.engine.raw_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def db_get_all_items(table):
    return as_cursor(f'SELECT * FROM {table}')

def db_get_all_items_with_constraints(table, constraints):
    return as_cursor(f'SELECT * FROM {table} WHERE {constraints}')

######## ADMIN ########

@app.route('/logout')
def logout():
    global CURRENT_USER
    if CURRENT_USER:
        flash(f'LOGGING OUT {CURRENT_USER}')
        CURRENT_USER = None
    return redirect(url_for('index'))

######## LOGIN/SIGNUP ########

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
