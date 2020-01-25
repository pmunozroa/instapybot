import requests as r
import random as rd
import json as js
from InstagramAPI import InstagramAPI as InstaAPI
import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)
from db.db import create_db, create_table, select_from, insert_into, get_db, close_connection
db_db = 'instagram'
db_table = 'pets_account'
db = get_db()
cursor = db.cursor()
create_db(cursor, db_db)
create_table(cursor, db_db, db_table)
tmp_img_path = 'pets.jpg'
upload_img_path = 'pets2.jpg'
instagram_username = 'pets_every_hour'
instagram_password = 'hola1313'
img_api_url = [(0, 'https://randomfox.ca/floof'),
               (1, 'https://api.thecatapi.com/v1/images/search'),
               (2, 'https://dog.ceo/api/breeds/image/random'),
               (3, 'https://aws.random.cat/meow'),
               (4, 'http://shibe.online/api/shibes'),
               (5, 'https://random.dog/woof.json'),
               (6, 'https://meme-api.herokuapp.com/gimme/aww'),
               ]
tags = '#animals #nature #animal #dog #pets #cute \
#dogs #pet #love #dogsofinstagram #instagram #photooftheday \
#photography #instagood #wildlife #puppy #petstagram #of #cat \
#cats #dogstagram #doglover #instadog #dogoftheday #adorable \
#ilovemydog #petsagram #naturephotography #animallovers #bhfyp'


def get_url(choice, content):
    if choice == 0:
        url = content['image']
    elif choice == 1:
        url = content[0]['url']
    elif choice == 2:
        url = content['message']
    elif choice == 3:
        url = content['file']
    elif choice == 4:
        url = content[0]
    elif choice in (5, 6):
        url = content['url']
    return url


def do_request():
    choice, api_url = rd.choice(img_api_url)
    response = r.get(api_url)
    if response.ok:
        data = js.loads(response.content)
        url = get_url(choice, data)
        return url
    else:
        return do_request()


def get_image():
    url = do_request()
    if ".jpg" not in url:
        return get_image()
    image = r.get(url)
    results = select_from(cursor, db_table, url)
    if url in results:
        return get_image()
    if image.ok:
        insert_into(cursor, db, db_table, url)
        return image.content
    else:
        return get_image()


def get_dimensions(height, width):
    if height > width:
        if height > 1000:
            height = 1000
        dimensions = [height, height]
        return dimensions
    else:
        if width > 1000:
            width = 1000
        dimensions = [width, width]
        return dimensions


def upload_image():
    Insta = InstaAPI(instagram_username, instagram_password)
    Insta.login()  # login
    Insta.uploadPhoto(upload_img_path, caption='{}'.format(tags))
    close_connection(cursor, db)
