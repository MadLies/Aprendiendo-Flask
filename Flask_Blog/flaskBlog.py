from flask import Flask, render_template
app = Flask(__name__)
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
	return render_template("about.html",posts=posts)

if __name__ == '__main__':
	app.run(debug=True)