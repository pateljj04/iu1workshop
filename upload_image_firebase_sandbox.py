#!/usr/bin/env python3

# Install firebase_admin
# * https://github.com/firebase/firebase-admin-python
# * `sudo pip3 install firebase-admin`
#
# Setup Firebase
# * https://console.firebase.google.com/
# * create a Firebase application
# * download your credentials .json and name it 'firebase-key.json'. Keep this file private.

import sys
import os
import requests
from mimetypes import guess_type
from time import strftime
import firebase_admin
from firebase_admin import credentials, storage

#image_url = sys.argv[1] #we pass the url as an argument

# TODO: Turn this into a function so image location/name can be passed and returns url.
# def upload_image(pi_image_name):

cred = credentials.Certificate('firebase-key.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'stem-workshop.appspot.com'
})

bucket = storage.bucket()

with open('stem.jpg','rb', buffering=0) as f:
    image_data = f.read()
    name, extension = os.path.splitext(f.name)
    content_type, _ = guess_type(f.name)

    # Add the time to the filename: 'stem-upload-2019-03-12-02-38-30-PM.jpg'
    filename = '%s-upload-%s%s' % (name, strftime('%Y-%m-%d-%I-%M-%S-%p'), extension)

blob = bucket.blob(filename)
blob.upload_from_string(image_data, content_type=content_type)
blob.make_public()

print(blob.public_url)
