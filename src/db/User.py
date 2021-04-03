class User:
    
    def __init__(self, username, type):
        self.username = username
        self.type = type

    def __repr__(self):
        return f"{self.username} -- {self.type}"
    
    def isAdmin(self):
        return self.type == 'Admin'
    
    def isCustomer(self):
        return self.type == 'Customer'
    
    def isEmployee(self):
        return self.type == 'Employee'