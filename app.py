import os
from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_table import Table, Col
from flask_sqlalchemy  import SQLAlchemy
from flask_migrate import Migrate


# from src.db.database import User
from __init__ import CURRENT_USER
from src.forms.forms import LoginForm, RecordForm, CustomerProfileForm, EmployeeProfileForm, AddHotelForm, AddHotelChainForm, RecordForm, SearchForm
from src.util.util import profile_is_set
from src.db.secret import password
from src.db.User import User

######## HARDCODED ########

LOGIN_ = {'admin':'admin12345' , 'employee': 'employee123', 'customer': 'customer123'}

######## HARDCODED ########


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
# # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or \
# #         'sqlite:///' + os.path.join(basedir, 'app.db')
# app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://fchis052:{password()}@web0.eecs.uottawa.ca:15432/group_a01_g44'
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

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
        print('TODO')
    
    return render_template('search.html', form=form)

@app.route('/view_all_customers')
def view_all_customers():
    global CURRENT_USER
    if not logged_in():
        return redirect(url_for('login'))
    elif not CURRENT_USER.isAdmin():
        flash(f'Unable to access page while logged in as {CURRENT_USER.type}')
        return redirect(url_for('index'))
    return render_template('view_all_customers.html', data=db_get_all_teams())

@app.route('/view_all_employees')
def view_all_employees():
    global CURRENT_USER
    if not logged_in():
        return redirect(url_for('login'))
    elif not CURRENT_USER.isAdmin():
        flash(f'Unable to access page while logged in as {CURRENT_USER.type}')
        return redirect(url_for('index'))
    return render_template('view_all_employees.html', data=db_get_all_teams())

@app.route('/view_hotels')
def view_hotels():
    global CURRENT_USER
    if not logged_in():
        return redirect(url_for('login'))
    elif not CURRENT_USER.isAdmin():
        flash(f'Unable to access page while logged in as {CURRENT_USER.type}')
        return redirect(url_for('index'))
    return render_template('view_hotels.html', data=db_get_all_teams())

@app.route('/view_records')
def view_records():
    global CURRENT_USER
    if not logged_in():
        return redirect(url_for('login'))
    elif not CURRENT_USER.isAdmin():
        flash(f'Unable to access page while logged in as {CURRENT_USER.type}')
        return redirect(url_for('index'))
    return render_template('view_records.html', data=db_get_all_teams())

@app.route('/view_room')
def view_room():
    global CURRENT_USER
    if not logged_in():
        return redirect(url_for('login'))
    elif not CURRENT_USER.isAdmin():
        flash(f'Unable to access page while logged in as {CURRENT_USER.type}')
        return redirect(url_for('index'))
    return render_template('view_room.html', data=db_get_all_teams())


def db_get_all_teams():
    return [['Temporary']]
######## ADMIN ########


# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     form = RegisterForm()

#     if form.validate_on_submit():
#         if not form.confirm.data == form.password.data:
#             return redirect(url_for('signup'))
#         hashed_password = generate_password_hash(form.password.data, method='sha256')
#         try: 
#             # SOME DB!!!
#             # new_user = User(username=form.username.data, email=form.email.data, password=hashed_password, instructor=form.instructor.data )
#             # db.session.add(new_user)
#             # db.session.commit()

#             flash('New user \'{}\' has been created!'.format(form.username.data))
#             flash('Please sign in {}!'.format(form.username.data))
#             return redirect(url_for('login'))
#         except:
#             flash('Something went wrong! The email address you entered may already be in use!'.format(form.username.data))
        

#     return render_template('signup.html', form=form)

@app.route('/logout')
def logout():
    global CURRENT_USER
    if CURRENT_USER:
        flash(f'LOGGING OUT {CURRENT_USER}')
        CURRENT_USER = None
    return redirect(url_for('index'))

######## LOGIN/SIGNUP ########

if __name__ == "__main__":
    # db.create_all()
    app.run(debug=True)
