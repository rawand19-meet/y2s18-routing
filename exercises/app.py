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
	
	student1 =session.query(
		Student).filter_by(
		student_id = student_id).first()
	
	return render_template('student.html' , n =student1)



app.run(debug=True)
