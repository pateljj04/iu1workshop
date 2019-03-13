#!/usr/bin/env python3

from time import strftime
import requests

timestamp = strftime('%Y-%m-%d-%I-%M-%S-%p')

# with open('stem.jpg','rb', buffering=0) as f:
#     image_data = f.read()

# Create an account
def create_user(username):
    url = 'http://localhost:3000/users.json'
    data = { 'username': username }
    response = requests.post(url, json=data)
    if response.ok:
        user_data = response.json()
        print('Created user', user_data)
    else:
        print("Oops! Couldn't create the user '%s'" % username)
        print(response.text)

# create_user(username='ahoyt')

# Upload an image to my account
def upload_user_avatar(user_id, filename):
    url = 'http://localhost:3000/users/%s.json' % user_id
    # headers = {'Content-type': 'multipart/form-data'}
    # data = { 'username': 'ahoyt', 'images': [] }
    # files = [ # this doesn't jive with the server
    #     # ('images', ('stem.jpg', open('stem.jpg', 'rb'), 'image/jpg'))
    #     ('images', open('stem.jpg', 'rb')),
    #     ('images', open('stem.jpg', 'rb'))
    # ]
    file = {'avatar': open(filename, 'rb')}
    response = requests.put(url, files=file)
    if response.ok:
        user_data = response.json()
        print('Updated user', user_data)
    else:
        print("Oops! Couldn't update user %s" % user_id)
        print(response.text)

# upload_user_avatar(user_id=1, filename='stem.jpg')

# Get my account
def get_user(user_id):
    url = 'http://localhost:3000/users/%s.json' % (user_id)
    response = requests.get(url)
    if response.ok:
        print('Got user', response.json())
    else:
        print("Oops! Couldn't get the user.", response.text)

# get_user(user_id=1)

def create_post(content, image_filename):
    url = 'http://localhost:3000/posts.json'
    data = { 'content': content }
    file = {'image': open(image_filename, 'rb')}
    response = requests.post(url, files=file, data=data)
    if response.ok:
        post = response.json()
        print('Created post', post)
        return post
    else:
        print("Oops! Couldn't create the post.")
        print(response.text)

# create_post('Test post', 'stem.jpg')

def ifttt(event, api_key, value1=None, value2=None, value3=None):
    ifttt_url = "https://maker.ifttt.com/trigger/%s/with/key/%s" % (event, api_key)
    payload   = { "value1" : value1, "value2" : value2, "value3" : value3 }
    response  = requests.post(ifttt_url, data=payload)
    if response.ok:
        print("Called IFTTT '%s' event." % (event))
    else:
        print("Oops! Couldn't send message to IFTTT.")
        print(response.text)

def post_and_send(message, image, ifttt_event, ifttt_api_key):
    post = create_post(message, image)
    if post:
        ifttt(ifttt_event, ifttt_api_key, post['content'], post['image_url'])

# post_and_send('Tweeting with Python and Ruby', 'stem.jpg', ifttt_event="create_post", ifttt_api_key="your-key-here")
