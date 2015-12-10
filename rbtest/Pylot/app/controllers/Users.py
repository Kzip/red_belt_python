"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.

            self.load_model('WelcomeModel')
        """
        self.load_model('User')
        self.load_model('Friend')

    """ This is an example of a controller method that will load a view for the client """
    def index(self):
        """
        A loaded model is accessible through the models attribute
        self.models['WelcomeModel'].get_all_users()
        """
        if 'user' not in session:
                session['user'] = None
        if 'ID' not in session:
                session['ID'] = None
        return self.load_view('index.html')

    def create(self):
        print "we got inside create"
        new_user = {
        "name":request.form['name'],
        "alias": request.form['alias'],
        "email" : request.form['email'],
        "pw" :  request.form['pwd']
        }
        self.models['User'].create_user(new_user)
        return redirect('/')

    def login(self):
        print "did we get to login?"
        user_info ={
        "email" : request.form['email'],
        "pw" :  request.form['pwd']
        }
        user_check = self.models['User'].login(user_info)
        if user_check == False:
            return redirect('/')
        '''if user_check['idusers'] == 1:
            print "we admin now"
            session['user'] = user_check['user_name']
            grab_users = self.models['User'].grab_all()
            return self.load_view('viewuser.html', users = grab_users)'''
        if  user_check:
            print "we logged in"
            session['user'] = user_check['ID']
            session['ID'] = user_check['name']
            print session['user']
            return redirect('/friends')
        else:
            print "we failed"
            return redirect('/')
    def friends(self):
        print session['user']
        #grab_msg = self.models['Message'].grab_all_posts_by(session['user'])
        grab_users = self.models['User'].grab_all(session['user'])
        #grab_not_friends = self.models['User'].grab_not_friends(session['user'])
        grab_friend = self.models['User'].grab_friends(session['user'])

        grab_not_friend = self.models['User'].grab_not_friends(session['user'])

        return self.load_view('friends.html', users = grab_users, friends = grab_friend, notfriends = grab_not_friend,login = session['ID'])
    def add(self,id):
        passed_info = {
        'user': session['user'],
        'friend': id
        }
        self.models['Friend'].add(passed_info)
        return redirect('/friends')
    def remove(self,id):
        passed_info = {
        'user': session['user'],
        'friend': id
        }
        self.models['Friend'].delete(passed_info)
        return redirect('/friends')
    def profile(self,id):
        grab_user = self.models['User'].grab_profile(id)
        return self.load_view('profile.html', user = grab_user)

    def logoff(self):
        session.clear()
        return redirect('/')
    def back(self):
        return redirect('/friends')
