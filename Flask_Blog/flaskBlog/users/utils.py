import os
import secrets
from PIL import Image
from flask import url_for , current_app
from flask_mail import Message
from flaskBlog import mail


def save_picture(form_picture):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_picture.filename)
	picture_fn = random_hex +f_ext
	picture_path= os.path.join(current_app.root_path , 'static/profile_pics', picture_fn)
	output_size = (125,125)
	with Image.open(form_picture) as i:
		i.thumbnail(output_size)
		i.save(picture_path)


	
	return picture_fn

def send_reset_email(user):
	token = user.get_reset_token()
	msg = Message('Password Reset Reques', sender = 'noreply@demo.com' ,recipients=[user.email] )
	msg.body = f'''Para resetear su correo visite el sigueinte link:
	{url_for('user.reset_token', token= token , _external= True )}

	Si no pediste esto , porfavor solo ignoralo tqm
	'''
	mail.send(msg)