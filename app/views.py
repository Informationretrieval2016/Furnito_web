from flask import Flask, render_template, request
from app import app
from models import Comments, Clicks
from common import Common
from search import Search

#start view controller
com = Common()
search = Search()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    datas = []
    search_query = request.form['srch-term']
    furniture_list = search.search_hardmatch(search_query)
    for furniture in furniture_list:
        data = com.readJSON(furniture)
        data['name'] = data['name'].replace('_',' ')
        if len(data['description']) >= 100:
            data['description'] = data['description'][:100] + '...'
        datas.append(data)
    return render_template('result.html', search_query = search_query, datas = datas)

@app.route('/show', methods=['GET', 'POST'])
def show():
    name = request.args.get('name').replace(' ','_')
    print name
    commentlist = []
    comments = Comments.query.filter_by(furniture_name = name).all()
    for comment in comments:
        commentlist.append(comment.comment)
    return render_template('show.html', commentlist = commentlist, name = name)

