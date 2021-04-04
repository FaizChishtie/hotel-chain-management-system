# hotel-chain-management-system
Hotel chain management system for CSI2132

## Team Members

Faizaan Chishtie 300008947

Omar Hayat 300096867

Tony Pei 8815641

## Startup

### First Step:

In the `CONFIG` file:

PLEASE replace:

```
USERNAME="myUsername"
PASSWORD="myPassword"
```

With your uOttawa username and password! This will create the PostgreSQL connection.


``` 
python3 app.py 
```

> Should be hosted on `127.0.0.1:5000`

There are 3 types of user:

> Since the goal of this project was not to create a full authentication mechanism, our group has decided to use pre-made accounts to demonstrate functionality

* Admin

```
username: admin
password: admin12345
```

Admin can add and remove hotel chains, add and remove customers and employees, and modify most database items.

* Employee

```
username: employee
password: employee123
```

Employee has a role and a profile, along with a hotel that they work for, they can create records to book customers should they come in.

> Although this specific employee won't have as much functionality as described - it is a way to demo the UI interacting with the DB

* Customer 

```
username: customer
password: customer123
```

Customers can browse hotel chains and view available bookings in the system. Their records will show up when an employee registers them in a room.


## To install

```
pip3 install --user flask sqlalchemy flask-sqlalchemy
pip3 install flask-bootstrap
pip3 install flask-wtf
pip3 install flask-login
pip3 install flask-table
pip install psycopg2-binary
```