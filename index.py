#import os to get file access methods
import os
#import random to for random image-chooser
from random import choice
#import flask framework stuff
from flask import Flask, render_template, request 

#create a new app and define the static content path
app = Flask(__name__, static_url_path = '/static', static_folder='static')
#create super-secure secret key for decoding some stored information
app.config['SECRET_KEY'] = 'ASDF'

#define method for top level route to show homepage
@app.route('/')
def show_home():
	#just return the template, there's no dynamic content here.
	return render_template('index.html') 


#define the route for playing the game
#grade is an integer arg defining which grade level they are playing
@app.route('/game/<grade>', methods=['GET', 'POST'])
def show_img(grade):
	#get the directory for the grade and choose a random image from it
	base = 'static/images/' + grade + '/'
	dirlist = os.listdir(base)
	image = choice(dirlist)
	filename = '/' + base + image

	#if there's a post request, also check their answer 
	if request.method == 'POST':
		#get answer from post request
		answer = request.form['answer']
		#get expected from post request
		expected = request.form['expected']
		expected = os.path.basename(expected)
		expected = os.path.splitext(expected)[0]
		#convert both to lowercase for accurate comparison
		expected = expected.lower()
		answer = answer.lower()
		#return template based on correctness of answer
		if answer == expected:
			return render_template('game.html', filename=filename, correct=True)
		else:
			return render_template('game.html', filename=filename, correct=False)
	#if answer is neither correct or incorrect, 
	#it's the first image, so just return the basic template
	return render_template('game.html', filename=filename)

		
#if this is run as a main, run the app
#launches local test server 
if __name__ == '__main__':
	#turn debug off for production
	app.run(debug=True)
