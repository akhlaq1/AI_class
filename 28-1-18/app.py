from flask import Flask, request, jsonify
from flask_pymongo import PyMongo 

app=Flask(__name__)
app.config['MONGO_DBNAME']='mitti'
app.config['MONGO_Uri']='mongodb://akhlaq:akhlaqblablabla'

mongo =PyMongo(app)

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        search = request.form['user']
        students = []
        records = mongo.db.users.find({'user':search})
        for user in records:
            students.append({'user':user['user'], 'password':user['pass']})
        return jsonify({'students':students})
    else:
        return '''
        <form action="post">
        <h2>Search</h2>
        <input type="text" name='user'>
        <input type="submit" value='search'>
        </form>
        '''



app.run(debug=True)
