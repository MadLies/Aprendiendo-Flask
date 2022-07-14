from flask import Flask, render_template, url_for , flash , redirect
from forms import RegistrationForm , LoginForm
app = Flask(__name__)
#import secrets
#secrets.token_hex(16)
app.config['SECRET_KEY'] = 'aff4a3b186f04ee3aef69e2bc888492c'
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


if __name__ == '__main__':
	app.run(debug=True)