import os
import secrets
from PIL import Image
from flask import url_for, current_app
#from flask_mail import Message
#from flaskblog import app, mail

def savePics(formPic):
    randomHex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(formPic.filename) # _ -> unused variable-value
    picture_name = randomHex + f_ext
    picturePath = os.path.join(current_app.root_path, 'static/profile_pics', picture_name)
    #resize uploaded-pics to 125px
    outputSize = (125, 125)
    i = Image.open(formPic)
    i.thumbnail(outputSize)
    
    i.save(picturePath)

    return picture_name

#send_reset_email goes here

#send_reset_password goes here