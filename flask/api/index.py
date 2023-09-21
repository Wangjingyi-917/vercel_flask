from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig') # define server
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#db = SQLAlchemy(app) # connect database

#from models import *


@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/design-projects/', methods=['GET'])
def de_projects():
    return render_template("design-projects.html")

@app.route('/research-projects/', methods=['GET'])
def re_projects():
    return render_template("research-projects.html")

@app.route('/members/', methods=['GET'])
def members():
    return render_template("members.html")

@app.route('/project1/', methods=['GET'])
def project1():
    return render_template("project1.html")

@app.route('/project2/', methods=['GET'])
def project2():
    return render_template("project2.html")

@app.route('/project3/', methods=['GET'])
def project3():
    return render_template("project3.html")
   

if __name__ == '__main__':
    app.run(debug=True)
