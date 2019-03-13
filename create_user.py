#!/usr/bin/env python3

import firebase_admin
from firebase_admin import credentials, storage

cred = credentials.Certificate('firebase-key.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'stem-workshop.appspot.com'
})

user = auth.create_user(display_name='IU 1 Workshop', email='iu1workshop@example.com', password='workshop')
print("Created user '%s' with uid %s" % (user.display_name, user.uid))

# user = auth.get_user(uid='uzk8GPjuWXfFoR7mSxnfSSt1oyG3')
user = auth.get_user_by_email(email='iu1workshop@example.com')
