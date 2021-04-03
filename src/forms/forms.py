from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectMultipleField, FloatField, DateField
from wtforms.validators import InputRequired, Email, Length, EqualTo, NumberRange


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    submit = SubmitField('Sign In')

class CustomerProfileForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(max=50)])
    address = StringField('Address', validators=[InputRequired(), Length(max=300)])
    sin_number = IntegerField('SIN Number', validators=[InputRequired(), Length(max=7)])
    submit = SubmitField('Create Profile')

class EmployeeProfileForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(max=50)])
    address = StringField('Address', validators=[InputRequired(), Length(max=300)])
    sin_number = IntegerField('SIN Number', validators=[InputRequired(), Length(max=10)])
    position = StringField('Position', validators=[InputRequired(), Length(max=50)])
    salary = FloatField('Position', validators=[InputRequired(), Length(max=50)])
    works_for = StringField('Works For', validators=[InputRequired(), Length(max=50)])
    submit = SubmitField('Create Profile')

class AddHotelForm(FlaskForm):
    n_rooms = IntegerField('Number of Rooms', validators=[InputRequired()])
    address = StringField('Address', validators=[InputRequired(), Length(max=300)])
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    phone_numbers = StringField('Phone Numbers (split by comma)', validators=[InputRequired(), Length(max=300)])
    chain = StringField('Chain Name', validators=[InputRequired(), Length(max=50)])
    n_stars = IntegerField('Star Number', validators=[NumberRange(1,5)])
    submit = SubmitField('Add Hotel to Hotel Chain')

class AddHotelChainForm(FlaskForm):
    address_of_hq = StringField('Address of HQ', validators=[InputRequired(), Length(max=300)])
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    phone_numbers = StringField('Phone Numbers (split by comma)', validators=[InputRequired(), Length(max=300)])
    submit = SubmitField('Create Hotel Chain')

class RecordForm(FlaskForm):
    room_type = StringField('Room Type', validators=[InputRequired()])
    n_occupants = IntegerField('Number of Occupants', validators=[InputRequired()])
    customer = StringField('Customer', validators=[InputRequired(), Length(max=300)])
    hotel_name = StringField('Hotel Name', validators=[InputRequired(), Length(max=300)])
    start_date = DateField('Start Date', format='%m/%d/%Y')
    end_date = DateField('End Date', format='%m/%d/%Y')
    submit = SubmitField('Create Record')

class SearchForm(FlaskForm):
    room_type = StringField('Room Type')
    n_occupants = IntegerField('Number of Occupants')
    hotel_chain = StringField('Hotel Chain')
    start_date = DateField('Start Date', format='%m/%d/%Y')
    end_date = DateField('End Date', format='%m/%d/%Y')
    n_stars = IntegerField('Star Number', validators=[NumberRange(1,5)])
    submit = SubmitField('Search')