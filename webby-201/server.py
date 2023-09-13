from flask import Flask, render_template, url_for, request, redirect
import json
app = Flask(__name__)
print(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

# @app.route("/thankyou.html/<data>")
# def thankyou_page(data = {}):
#     print(f"received: {data}")
#     data_json = json.dumps(data)
#     print(f"received : {data_json}")
#     email = data_json[0]
#     print(f"email : {email}")
#     return render_template("thankyou.html", email = email)

def write_to_file(data):
    with open("database.txt", mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email},{subject},{message}")    

@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        print(f"posted: {data}")
        write_to_file(data)
        # return "form submitted"
        # return redirect(url_for('thankyou_page', data = data))
        return redirect("thankyou.html")
    else:
        return "something went wrong. try again!"

# @app.route("/index.html")
# def my_index():
#     return render_template("index.html")

# @app.route("/about.html")
# def my_about():
#     return render_template("about.html")

# @app.route("/work.html")
# def my_work():
#     return render_template("work.html")

# @app.route("/works.html")
# def my_works():
#     return render_template("works.html")

# @app.route("/components.html")
# def my_components():
#     return render_template("components.html")

# @app.route("/contact.html")
# def my_contact():
#     return render_template("contact.html")

# @app.route("/thankyou.html")
# def my_thank_you():
#     return render_template("thankyou.html")