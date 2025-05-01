from flask import Flask, render_template, redirect, url_for
from job import Jobs


app = Flask(__name__)  


@app.route('/') 
def home():
  return render_template('home.html',jobs=Jobs[:10])


@app.route('/api/jobs')
def list_jobs():    
  return Jobs[:10]



if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)