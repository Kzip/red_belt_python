"""
    Sample Model File

    A Model should be in charge of communicating with the Database.
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re

class User(Model):
    def __init__(self):
        super(User, self).__init__()
    """
    Below is an example of a model method that queries the database for all users in a fictitious application

    def get_all_users(self):
        print self.db.query_db("SELECT * FROM users")

    Every model has access to the "self.db.query_db" method which allows you to interact with the database
    """
    def create_user(self,info):
        # in the model function we will write our validations
        # they will look very similar to those we wrote in simple Flask
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
       # some basic validations
        if not info['name']:
           errors.append('Name cannot be blank')

        elif len(info['name']) < 2:
           errors.append('Name must be at least 2 characters long')

        if not info['email']:
           errors.append('Email cannot be blank')

        elif not EMAIL_REGEX.match(info['email']):
           errors.append('Email format must be valid!')

        if not info['pw']:
           errors.append('Password cannot be blank')

        elif len(info['pw']) < 8:
           errors.append('Password must be at least 8 characters long')

        '''elif info['password'] != info['pw_confirmation']:
         errors.append('Password and confirmation must match!')'''
      # check if there are any errors, if there are any return the array
       # otherwise return True
        if errors:
         return {"status": False, "errors": errors}
        else:
         # code to insert user goes here
         # retrieve the last inserted user
         password = info['pw']
         hashed_pw = self.bcrypt.generate_password_hash(password)
         query = "INSERT INTO users (name, alias, email, pw) VALUES ('{}','{}','{}','{}')".format(info['name'],info['alias'],info['email'],hashed_pw)
         self.db.query_db(query)

         get_user_query = "SELECT * FROM users ORDER BY ID DESC LIMIT 1"
         user = self.db.query_db(get_user_query)
          #return {"status": True, "user": user[0]}
         return user
    def login(self,info):
     EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
     errors = []
     if not info['email']:
       errors.append('Email cannot be blank')
       print "we should get this error"
       return False

     elif not EMAIL_REGEX.match(info['email']):
       errors.append('Email format must be valid!')
     if errors:

         return {"status": False, "errors": errors}
     else:
        print "do we get in here"
        password = info['pw']
        user_query = "SELECT * FROM users WHERE email = '{}' LIMIT 1".format(info['email'])
        users = self.db.query_db(user_query)
        if users[0]:
           # check_password_hash() compares encrypted password in DB to one provided by user logging in
            if self.bcrypt.check_password_hash(users[0]['pw'], password):
                return users[0]
        return False

    def grab_all(self, id_of_user):
            query = "SELECT * FROM users WHERE users.ID !='{}';".format(id_of_user)
            all = self.db.query_db(query)
            return all
    def grab_friends(self, id):
        query = "SELECT * FROM users LEFT JOIN friends on users.ID = friends.users_ID LEFT JOIN users as users2 ON users2.ID = friends.friend_ID WHERE users.ID = '{}'".format(id)
        all = self.db.query_db(query)
        return all
    def grab_not_friends(self,id):
        query = "SELECT users.ID as `User ID`, users2.name, users2.ID, users2.email, users2.alias  FROM users  JOIN users as users2 ON users.ID <> users2.id  LEFT JOIN friends  ON users.ID = friends.users_ID AND users2.ID = friends.friend_ID  WHERE friends.friend_ID IS NULL and  users.ID = '{}'".format(id)
        all = self.db.query_db(query)
        return all
    def grab_profile(self,id):
        query = "SELECT * FROM users WHERE users.ID ='{}';".format(id)
        user = self.db.query_db(query)
        return user
    """
    If you have enabled the ORM you have access to typical ORM style methods.
    See the SQLAlchemy Documentation for more information on what types of commands you can run.
    """
