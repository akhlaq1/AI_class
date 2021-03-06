from flask import Flask, render_template,send_file,url_for,request

app=Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/form")
def form():
    return render_template('form.html')


@app.route("/user/<name>")
def user(name):
    return "Hello Dear :"+name


@app.route("/info",methods=['GET','POST'])
def info(name):
    if request.method=="GET":
        return "Hello GET waalo"+request.form['user']
    else:
        return "Hello POST waalo"+request.form['user']


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/image")
def image():
    return send_file('image.jpeg')



app.run(debug=True)
