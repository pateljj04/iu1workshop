#!/usr/bin/env python3

# Not pyrebase, which uses an old version of requests.
# * https://github.com/thisbejim/Pyrebase
# * pip3 install pyrebase

# Install Python Firebase
# * https://github.com/ozgur/python-firebase
# * pip3 install requests
# * pip3 install python-firebase
#   - has bug, so for now install from github
#     pip3 install git+https://github.com/ozgur/python-firebase

from firebase import firebase

# Get this from Project Overview.
config = {
    "apiKey": "AIzaSyBpa2mGMtz98w89rbCmsNF2lWjpA6I1DJs",
    "authDomain": "stem-workshop.firebaseapp.com",
    "databaseURL": "https://stem-workshop.firebaseio.com",
    "projectId": "stem-workshop",
    "storageBucket": "stem-workshop.appspot.com",
    "messagingSenderId": "90372049063"
}

firebase_app = firebase.FirebaseApplication('https://stem-workshop.firebaseio.com', None)


# Authenticating with secrets is a legacy behavior.
# https://www.firebase.com/docs/rest/guide/user-auth.html
firebase_secret = 'firebase-key.json'
authentication = firebase.FirebaseAuthentication(firebase_secret, 'iu1workshop@example.com', extra={'id': 'uzk8GPjuWXfFoR7mSxnfSSt1oyG3'})
firebase.authentication = authentication
print(authentication.extra)

user = authentication.get_user()
print(user.firebase_auth_token)

result = firebase_app.get('/users', 'uzk8GPjuWXfFoR7mSxnfSSt1oyG3')
print(result)
