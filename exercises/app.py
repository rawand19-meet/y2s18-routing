from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home ():
    return render_template('home.html')

#@app.route('/hello')
#def hello():
 
#  return 'Hello, World'

@app.route('/<int:student_id>')
def yeah(student_id):
	return render_template('student.html')


app.run(debug=True)
