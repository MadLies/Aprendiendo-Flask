from flask import render_template, url_for, flash, redirect
from flaskBlog import app
from flaskBlog.models import User, Post
from flaskBlog.forms import RegistrationForm, LoginForm


#diccionarios


posts = [ 
	{
		'author': 'wilchitos',
		'title': 'Post 1',
		'content' : 'Content1',
		'date_posted': 'Noviembre 20, 2022'
	},

	{
		'author': 'pepe',
		'title': 'Post 2',
		'content' : 'Content2',
		'date_posted': 'Noviembre 23, 2022'
	}
]
#acceso a las rutas 
@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html",posts=posts)

@app.route("/about")
def about():
	return render_template("about.html",title = "about")

@app.route("/register", methods= ['GET', 'POST'])
def register():
		form = RegistrationForm()
		if form.validate_on_submit():
			flash(f'Accout created for {form.username.data}!','success')
			return redirect(url_for('home'))
		return render_template('register.html' ,title = "Register", form=form )

@app.route("/login" , methods= ['GET', 'POST'])
def login():
		form = LoginForm()
		if form.validate_on_submit():
			if form.email.data == "hola@gmail.com" and form.password.data == "1234" :
				flash("holiii ", "success")
				return redirect(url_for('home'))
			else:
				flash("puto") 

		return render_template('login.html' ,title = "Login", form=form )

