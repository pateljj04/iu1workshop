#!/usr/bin/env python
import sys
import os
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

#image_url = sys.argv[1] #we pass the url as an argument

cred = credentials.Certificate('firebase-key.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'stem-workshop.appspot.com'
})
bucket = storage.bucket()

my_image = open('stem.jpg','rb', buffering=0)
image_data = my_image.read()

blob = bucket.blob('nameoffile.jpg')

blob.upload_from_string(
        image_data,
        content_type='image/jpg'
    )
blob.make_public()
print(blob.public_url)
