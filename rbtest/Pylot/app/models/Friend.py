"""
    Sample Model File

    A Model should be in charge of communicating with the Database.
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re

class Friend(Model):
    def __init__(self):
        super(Friend, self).__init__()

    def add(self,passedinfo):
        print "____"
        print passedinfo['user']
        print passedinfo['friend']
        print"____"
        query = "INSERT INTO `mydb`.`friends` (`users_ID`, `friend_ID`) VALUES ('{}', '{}');".format(passedinfo["user"],passedinfo['friend'])
        self.db.query_db(query)
        return
    def delete(self,passedinfo):
        print "____"
        print passedinfo['user']
        print passedinfo['friend']
        print"____"
        query = "DELETE FROM `mydb`.`friends` WHERE `users_id`='{}' and friend_ID ='{}';".format(passedinfo["user"],passedinfo['friend'])
        self.db.query_db(query)
        return
