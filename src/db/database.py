# from flask_migrate import Migrate
# from flask_sqlalchemy  import SQLAlchemy
# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
# from flask_table import Table, Col
# from src.db.secret import password
# import os

# # db = None

# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(15), unique=True)
#     email = db.Column(db.String(50), unique=True)
#     password = db.Column(db.String(80))
#     instructor = db.Column(db.Boolean)

#     def __repr__(self):
#         return 'User {} Instructor {}'.format(self.username, str(bool(self.instructor)))

# class Student(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(15), unique=True)
#     student_number = db.Column(db.String(15))
#     program = db.Column(db.String(80))

#     def __repr__(self):
#         return "<Student: {}>".format(self.student_number)

# class TeamParameter(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     max_size = db.Column(db.Integer)
#     min_size = db.Column(db.Integer)
#     active = db.Column(db.Boolean)

# class RequestForTeam(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(15))
#     team_name = db.Column(db.String(30))

# class TeamsList(db.Model):
#     __tablename__ = "teams_list"
#     id = db.Column(db.Integer, primary_key=True)
#     team_name = db.Column(db.String(30))
#     username = db.Column(db.String(15))
#     liaison = db.Column(db.Boolean)

#     def __repr__(self):
#         return "<Team Name: {}>".format(self.team_name)

# def as_cursor(query):
#     connection = db.engine.raw_connection()
#     cursor = connection.cursor()
#     cursor.execute(query)
#     return cursor.fetchall()

# def db_get_teams_for_user(username):
#     return as_cursor('SELECT team_name FROM teams_list WHERE username is \'{}\''.format(username))

# def db_get_open_teams_for_user(username):
#     return as_cursor('SELECT team_name FROM teams_list WHERE username is NOT\'{}\''.format(username))

# def db_get_user_requests(username):
#     return as_cursor('SELECT team_name FROM request_for_team WHERE username is \'{}\''.format(username))

# def db_pack_users_in_team(team_name):
#     _dict = {
#         'team_name' : team_name,
#         'retrieved' : db_retrieve_users_in_team(team_name),
#         'size' : db_count_members_in_team(team_name)
#     }
#     return _dict

# def db_count_members_in_team(team_name):
#     return as_cursor('SELECT COUNT(teams_list.username) FROM teams_list WHERE teams_list.team_name is \'{}\''.format(team_name))

# def db_retrieve_users_in_team(team_name):
#     return as_cursor('SELECT teams_list.username, student.student_number, student.program FROM teams_list INNER JOIN student ON teams_list.username=student.username WHERE teams_list.team_name is \'{}\''.format(team_name))

# def db_get_team_names():
#     return as_cursor('SELECT DISTINCT team_name FROM teams_list')

# def db_get_all_teams():
#     formattable = []
#     for pair in db_get_team_names():
#         t_name = pair[0]
#         formattable.append(db_pack_users_in_team(t_name))
#     return formattable

# def db_user_in_team(team_name, username):
#     return not as_cursor('SELECT COUNT(teams_list.username) FROM teams_list WHERE teams_list.team_name is \'{}\' AND teams_list.username is \'{}\''.format(team_name,username))[0][0] == 0

# def db_all_liason_for_user(username):
#     return as_cursor('SELECT team_name FROM teams_list WHERE username is \'{}\' AND liaison'.format(username))

# def user_is_liaison_for(team_name, username):
#     return not (as_cursor('SELECT COUNT(teams_list.team_name) FROM teams_list WHERE username is \'{}\' AND liaison'.format(username))[0][0] == 0)

# def db_pack_users_in_requests(team_name):
#     _dict = {
#         'team_name' : team_name,
#         'retrieved' : db_retrieve_users_in_request_where_liaison(team_name),
#     }
#     return _dict

# def db_retrieve_users_in_request_where_liaison(team_name):
#     return as_cursor('SELECT username FROM request_for_team WHERE team_name is \'{}\''.format(team_name))

# def db_get_all_requests(username):
#     formattable = []
#     for pair in db_all_liason_for_user(username):
#         t_name = pair[0]
#         formattable.append(db_pack_users_in_requests(t_name))
#     return formattable

# def user_exists(username):
#     return not (as_cursor('SELECT COUNT(student.username) FROM student WHERE username is \'{}\''.format(username))[0][0] == 0)


# ####

# # def db_setup(app, basedir):
# #     app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
# #     # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or \
# #     #         'sqlite:///' + os.path.join(basedir, 'app.db')
# #     app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://fchis052:{password()}@web0.eecs.uottawa.ca:15432/group_a01_g44'
# #     db = SQLAlchemy(app)
# #     migrate = Migrate(app, db)
# #     return db

#     #