import requests as r
import random as rd
import json as js
from InstagramAPI import InstagramAPI as InstaAPI
import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)
from db.db import create_db, create_table, select_from, insert_into, get_db, close_connection
db_db = 'instagram'
db_table = 'creepy_account'
db = get_db()
cursor = db.cursor()
create_db(cursor, db_db)
create_table(cursor, db_db, db_table)
tmp_img_path = 'tmpcreepy.jpg'
upload_img_path = 'tmp2creepy.jpg'
instagram_username = 'creepy__art__gram'
instagram_password = 'hola1313'
img_api_url = [(0, 'https://meme-api.herokuapp.com/gimme/CreepyArt'),
               (1, 'https://meme-api.herokuapp.com/gimme/Scary'),
               (2, 'https://meme-api.herokuapp.com/gimme/creepy'), ]
tags = '#scary #horror #creepy #halloween #horrormovies \
#art #spooky #ghost #dark #funny #memes #creepypasta \
# #blood #love #meme #horrorfan #horrormovie #photography \
# #gore #scarystories #horrorstories #makeup #haunted \
# #movie #nightmare #drawing #paranormal #goth #film #bhfyp'


def get_url(choice, content):
    if choice in (0, 1, 2):
        url = content['url']
    # elif choice == 1:
    #    url = content[0]['url']
    # elif choice == 2:
    #    url = content['message']
    # elif choice == 3:
    #    url = content['file']
    # elif choice == 4:
    #    url = content[0]
    # elif choice == 5:
    #    url = content['url']
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
    Insta.login()
    Insta.uploadPhoto(upload_img_path, caption='{}'.format(tags))
    close_connection(cursor, db)
