from flask import Flask, render_template, url_for
app = Flask(__name__)
print(__name__)

@app.route("/")
def hello_world():
    # return "Hello!!!!"
    # print({{ url_for('static', filename='favicon.ico') }})
    return render_template("index.html")

@app.route("/<username>")
def hello_user(username=None):
    return render_template("index.html", name=username)

@app.route("/<username>/<int:post_id>")
def hello_user_post(username=None, post_id=None):
    return render_template("index.html", name=username, post_id=post_id)

@app.route("/about.html")
def about():
    # return "Hello!!!!"
    return render_template("about.html")

@app.route("/blog")
def blog():
    return "This are my thoughts on blog"

@app.route("/blog/2020/dogs")
def blog2():
    return "This is my dog"