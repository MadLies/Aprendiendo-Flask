from flask import Flask, render_template, url_for
from forms import RegistraitionFrom , LoginFrom
app = Flask(__name__)

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

@app.route("/register")
	def register():
		form = RegistraitionFrom()
		return render_template('register.html' ,title = "Register", form=form )

@app.route("/login")
	def login():
		form = LoginFrom()
		return render_template('login.html' ,title = "login", form=form )


if __name__ == '__main__':
	app.run(debug=True)