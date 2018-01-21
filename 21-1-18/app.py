from flask import Flask, render_template,send_file,url_for

app=Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/user/<name>")
def user(name):
    return "Hello Dear :"+name


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/image")
def image():
    return send_file('image.jpeg')



app.run(debug=True)
