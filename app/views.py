from flask import Flask, render_template, request
from 
from app import app

#start view controller
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result')
def result():
	search_query = request.form['srch-term']
	return render_template('result.html')

@app.route('/show')
def show():
	commentlist = comment.query.filter_by(furniture_name = ).all()
